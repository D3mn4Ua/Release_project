document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('theme-toggle');
    const body = document.body;
    const root = document.documentElement;
    const logo = document.getElementById('logo');

    function getStoredTheme() {
        try {
            const storedTheme = localStorage.getItem('theme');
            if (storedTheme === 'dark' || storedTheme === 'light') return storedTheme;
        } catch (error) {
            console.warn('Failed to read theme setting:', error);
        }
        return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    function updateLogo(theme) {
        if (!logo) return;
        const newSrc = theme === 'dark' ? logo.dataset.darkLogo : logo.dataset.lightLogo;
        if (newSrc) logo.src = newSrc;
    }

    function applyTheme(theme) {
        const isDark = theme === 'dark';
        body.classList.toggle('dark-theme', isDark);
        body.classList.toggle('light-theme', !isDark);
        root.setAttribute('data-bs-theme', isDark ? 'dark' : 'light');
        root.style.colorScheme = isDark ? 'dark' : 'light';

        if (btn) {
            btn.classList.toggle('is-dark', isDark);
            const icon = btn.querySelector('i');
            if (icon) {
                icon.classList.toggle('bi-moon-stars-fill', !isDark);
                icon.classList.toggle('bi-sun-fill', isDark);
            }
            btn.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');
        }
        updateLogo(theme);
        try { localStorage.setItem('theme', theme); } catch (e) {}
    }

    applyTheme(getStoredTheme());

    if (btn) {
        btn.addEventListener('click', () => {
            const currentTheme = root.getAttribute('data-bs-theme');
            applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
        });
    }

    const filterForm = document.getElementById('filter-form');
    const categorySelect = document.getElementById('category-select');
    const filtersBlock = document.getElementById('filters-block');
    const productsContainer = document.getElementById('products-container');
    const paginationContainer = document.getElementById('pagination-container');
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    const resetBtn = document.getElementById('reset-filters');

    async function fetchProducts(page = 1) {
        productsContainer.style.opacity = '0.5';
        
        const formData = new FormData(filterForm);
        const params = new URLSearchParams(formData);
        
        if (searchInput && searchInput.value) {
            params.set('q', searchInput.value);
        }
        params.set('page', page);

        try {
            const response = await fetch(`?${params.toString()}`, {
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });

            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            
            const data = await response.json();
            productsContainer.innerHTML = data.products_html;
            paginationContainer.innerHTML = data.pagination_html;
            
            window.history.pushState({}, '', `?${params.toString()}`);
        } catch (error) {
            console.error('Failed to load products:', error);
        } finally {
            productsContainer.style.opacity = '1';
        }
    }

    async function loadCategoryFilters(categoryId) {
        if (!categoryId) {
            filtersBlock.replaceChildren();
            return;
        }

        filtersBlock.innerHTML = '<div class="text-muted small">Loading filters...</div>';

        try {
            const response = await fetch(`/get_category_filters/?category=${encodeURIComponent(categoryId)}`, {
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });

            if (!response.ok) throw new Error(`HTTP ${response.status}`);

            const data = await response.json();
            const fragment = document.createDocumentFragment();

            for (const [attr, values] of Object.entries(data)) {
                const wrapper = document.createElement('div');
                
                const label = document.createElement('label');
                label.className = 'form-label fw-medium small mb-1';
                label.textContent = `${attr}:`;

                const select = document.createElement('select');
                select.name = attr;
                select.className = 'form-select form-select-sm';

                const placeholder = document.createElement('option');
                placeholder.value = '';
                placeholder.textContent = `-- Select ${attr} --`;
                select.appendChild(placeholder);

                values.forEach(val => {
                    if (val !== null && val !== undefined && val !== '') {
                        const opt = document.createElement('option');
                        opt.value = val;
                        opt.textContent = val;
                        select.appendChild(opt);
                    }
                });

                wrapper.appendChild(label);
                wrapper.appendChild(select);
                fragment.appendChild(wrapper);
            }

            filtersBlock.replaceChildren(fragment);
        } catch (error) {
            console.error('Failed to fetch filters:', error);
            filtersBlock.innerHTML = '<div class="text-danger small">Failed to load filters.</div>';
        }
    }

    if (categorySelect) {
        categorySelect.addEventListener('change', (e) => loadCategoryFilters(e.target.value));
    }

    if (filterForm) {
        filterForm.addEventListener('submit', (e) => {
            e.preventDefault();
            fetchProducts(1);
        });
    }

    if (searchBtn) {
        searchBtn.addEventListener('click', () => fetchProducts(1));
    }
    
    if (searchInput) {
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                fetchProducts(1);
            }
        });
    }

    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            filterForm.reset();
            filtersBlock.replaceChildren();
            if (searchInput) searchInput.value = '';
            fetchProducts(1);
        });
    }

    document.addEventListener('click', (e) => {
        const pageLink = e.target.closest('.ajax-page-link');
        if (pageLink) {
            e.preventDefault();
            const page = pageLink.dataset.page;
            fetchProducts(page);
        }
    });
});