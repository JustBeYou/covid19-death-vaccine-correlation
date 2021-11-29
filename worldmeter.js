function getData() {
  const table = document.getElementById("main_table_countries_today");
    const rows = table.querySelectorAll("tr.odd:not(.total_row_world), tr.even:not(.total_row_world)");
    const data = [];
    for (const row of rows) {
        const cols = Array.from(row.querySelectorAll("td"));
        data.push(cols.map(col => col.innerText));
    }
    return data;
};