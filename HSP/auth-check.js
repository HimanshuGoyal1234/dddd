(async () => {
  try {
    const response = await fetch("/check-auth");
    const data = await response.json();
    
    if (!data.loggedIn) {
      window.location.href = "/";
    }
  } catch (error) {
    console.error("Auth check failed:", error);
    window.location.href = "/";
  }
})();