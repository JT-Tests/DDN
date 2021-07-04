const { NotFound, GeneralError } = require("../../helpers/errors");
const Sepulca = require("./sepulca.model");

class SepulcaServices {
    async getAll() {
        try {
            const sepulcas = await Sepulca.find({});
            return sepulcas;
        } catch (error) {
            throw new GeneralError("Sepulca Error");
        }
    }

    async getOne(id) {
        const sepulca = await Sepulca.findById(id);
        if (!sepulca) throw new NotFound("Sepulca not found");
        return sepulca;
    }

    async createSepulca(data) {
        try {
            const sepulca = new Sepulca(data);
            await sepulca.save();
            return sepulca;
        } catch (error) {
            throw new GeneralError("Sepulca Error");
        }
    }

    async updateSepulca(id, data) {
        const sepulca = await Sepulca.findByIdAndUpdate(id, data, { new: true });
        if (!sepulca) throw new NotFound("Sepulca not found");
        return sepulca;
    }

    async deleteSepulca(id, data) {
        await Sepulca.findByIdAndDelete(id, data);
    }
}

module.exports = new SepulcaServices();
