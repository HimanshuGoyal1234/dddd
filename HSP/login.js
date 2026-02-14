document.getElementById("passwordInput").addEventListener("keydown", async e => {
  if (e.key !== "Enter") return;

  const res = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password: e.target.value })
  });

  const data = await res.json();

  if (data.success) {
    // 🔥 CHANGE: Login time localStorage mein save kar rahe hain
    localStorage.setItem('loginTime', new Date().getTime().toString());

    const redirect =
      sessionStorage.getItem("originalUrl") || "HSP_interface.html";
    sessionStorage.removeItem("originalUrl");
    location.href = redirect;
  } else {
    alert("ACCESS DENIED");
  }
});