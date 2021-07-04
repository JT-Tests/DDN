const SepulcaServices = require("./sepulca.services");

class SepulcaController {
    async getAll(req, res, next) {
        try {
            const sepulcas = await SepulcaServices.getAll();
            return res.json(sepulcas);
        } catch (error) {
            next(error);
        }
    }

    async get(req, res, next) {
        try {
            const sepulcas = await SepulcaServices.getOne(req.params.sepulcaId);
            return res.json(sepulcas);
        } catch (error) {
            next(error);
        }
    }

    async create(req, res, next) {
        try {
            const sepulca = await SepulcaServices.createSepulca(req.body);
            return res.json(sepulca);
        } catch (error) {
            next(error);
        }
    }

    async update(req, res, next) {
        try {
            const sepulca = await SepulcaServices.updateSepulca(req.params.sepulcaId, req.body);
            return res.json(sepulca);
        } catch (error) {
            next(error);
        }
    }

    async delete(req, res, next) {
        try {
            await SepulcaServices.deleteSepulca(req.params.sepulcaId);
            return res.json("deleted successfully");
        } catch (error) {
            next(error);
        }
    }
}

module.exports = new SepulcaController();
