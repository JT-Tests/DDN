const mongoose = require("mongoose");

const sepulca = new mongoose.Schema(
    {
        name: {
            type: String,
            required: true,
        },
    },
    { timestamps: { createdAt: true, updatedAt: true } }
);

const Sepulca = mongoose.model("sepulca", sepulca);

module.exports = Sepulca;
