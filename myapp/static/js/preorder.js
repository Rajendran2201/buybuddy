function filterMenu() {
  let searchValue = document.getElementById("search-bar").value.toLowerCase();
  let filterValue = document.getElementById("category-filter").value;
  let menuItems = document.querySelectorAll(".menu-item");

  menuItems.forEach(item => {
      let itemName = item.getAttribute("data-name");
      let itemCategory = item.getAttribute("data-category");

      if ((itemName.includes(searchValue) || searchValue === "") &&
          (filterValue === "all" || itemCategory === filterValue)) {
          item.style.display = "block";
      } else {
          item.style.display = "none";
      }
  });
}
