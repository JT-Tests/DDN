const express = require("express");
const app = express();
const handleErrors = require("./middlewares/handleErrors");

const api = require("./api");
require("../data/database/db");

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/api", api);

app.use(handleErrors);

module.exports = app;
