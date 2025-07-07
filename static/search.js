function performSearch() {
  const query = document.getElementById("searchInput").value;
  fetch(`/search?q=${encodeURIComponent(query)}`)
    .then(response => response.json())
    .then(data => {
      const tbody = document.querySelector("tbody");
      if (!tbody) {
        // Optional: alert or redirect to /entries if you want
        alert("Search is only available on the 'View Entries' page.");
        return;
      }

      tbody.innerHTML = "";
      data.forEach((entry, index) => {
        tbody.innerHTML += `
          <tr>
            <td>${index + 1}</td>
            <td>${entry.date}</td>
            <td>${entry.type}</td>
            <td>${entry.tape}</td>
            <td>${entry.batch}</td>
            <td>${entry.remarks}</td>
          </tr>`;
      });
    });
}
