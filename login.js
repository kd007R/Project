
const express = require("express");
const session = require("express-session");
const mongoose = require("mongoose");
const bcrypt = require("bcrypt");

const app = express();

mongoose.connect("mongodb://localhost/bike_selling_website", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const UserSchema = new mongoose.Schema({
  username: String,
  password: String,
});


const User = mongoose.model("User", UserSchema);

// Configure Express app
app.use(express.urlencoded({ extended: true }));
app.use(
  session({
    secret: "bike selling website",
    resave: false,
    saveUninitialized: true,
  })
);


app.get("/login", (req, res) => {
  res.send(`
    <h1>Login</h1>
    <form method="post" action="/login">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required><br><br>
      <button type="submit">Login</button>
    </form>
  `);
});

app.post("/login", async (req, res) => {
  const { username, password } = req.body;


  const user = await User.findOne({ username });

  if (user) {
    // Check if password is correct
    if (await bcrypt.compare(password, user.password)) {
      req.session.userId = user._id;
      res.redirect("/");
    } else {
      res.send("Incorrect password");
    }
  } else {
    res.send("User does not exist");
  }
});


app.get("/logout", (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      console.log(err);
    } else {
      res.redirect("/");
    }
  });
});


const requireLogin = (req, res, next) => {
  if (req.session && req.session.userId) {
    next();
  } else {
    res.redirect("/login");
  }
};


app.get("/", requireLogin, (req, res) => {
  res.send(`
    <h1>Welcome to Bike Selling Website!</h1>
    <p>You are logged in as ${req.session.userId}</p>
    <a href="/logout">Logout</a>
  `);
});

// Start server
app.listen(3000, () => {
  console.log("Server started on port 3000");
});
