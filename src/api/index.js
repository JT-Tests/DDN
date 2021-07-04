const router = require("express").Router();

const sepulca = require("./sepulca/sepulca.routes");

router.use("/sepulca", sepulca);

module.exports = router;
