const bcrypt = require("bcrypt");

exports.generateHash = async (password) => {
	return await bcrypt.hash(password, 12);
};
