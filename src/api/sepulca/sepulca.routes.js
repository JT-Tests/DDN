const router = require("express").Router();

const SepulcaController = require("./sepulca.controllers");

router.get("/getAll", SepulcaController.getAll);
router.get("/get/:sepulcaId", SepulcaController.get);
router.post("/add", SepulcaController.create);
router.patch("/update/:sepulcaId", SepulcaController.update);
router.delete("/delete/:sepulcaId", SepulcaController.delete);

module.exports = router;
