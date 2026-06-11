const dateEl = document.getElementById("date");

if (dateEl) {
  const today = new Date();
  dateEl.textContent = today.toLocaleDateString(undefined, {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
}
