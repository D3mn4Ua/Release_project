document.addEventListener("DOMContentLoaded", function() {
    const categorySelect = document.getElementById("category-select");
    const filtersBlock = document.getElementById("filters-block");

    categorySelect.addEventListener("change", function() {
        const categoryId = this.value;

        if (!categoryId) {
            filtersBlock.innerHTML = "";
            return;
        }

        fetch(`/get_category_filters/?category=${categoryId}`)
            .then(response => response.json())
            .then(data => {
                let html = "";
                for (const [attr, values] of Object.entries(data)) {
                    html += `<fieldset><legend>${attr}:</legend><select name="${attr}">`;
                    html += `<option value="">-- вибрати ${attr} --</option>`;
                    values.forEach(v => {
                        if (v) {
                            html += `<option value="${v}">${v}</option>`;
                        }
                    });
                    html += `</select></fieldset>`;
                }
                filtersBlock.innerHTML = html;
            ;

            })
            .catch(err => {
                console.error("Failed to fetch the filters:", err);
            });
    });
});
