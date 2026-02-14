const express = require("express");
const session = require("express-session");
const path = require('path');

const app = express();
app.use(express.json());

// HSP folder se static files (like HSP_interface.html) serve karo
app.use(express.static("HSP"));

// Session middleware with 5 minute timeout
app.use(
  session({
    secret: "hsp_simple_secret",
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 5 * 60 * 1000 } // 5 minutes
  })
);

// Simple password (in production, use a more secure method)
const VALID_PASSWORD = "Wolf And Madara Uchiha";

// Login route
app.post("/login", (req, res) => {
  const { password } = req.body;
  
  if (password === VALID_PASSWORD) {
    req.session.loggedIn = true;
    res.json({ success: true });
  } else {
    res.json({ success: false, message: "Invalid password" });
  }
});

// Check authentication route
app.get("/check-auth", (req, res) => {
  res.json({ loggedIn: !!req.session.loggedIn });
});

// Logout route
app.post("/logout", (req, res) => {
  req.session.destroy(() => {
    res.json({ success: true });
  });
});

// Serve the password page as default (ROOT FOLDER SE)
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "HSP", "HSP_password.html"));
});
app.listen(3000, () => {
  console.log("🔥 Server running on http://localhost:3000");
});