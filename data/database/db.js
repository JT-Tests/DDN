require("dotenv").config();
const mongoose = require("mongoose");

(async () => {
    (async () => {
        const timeout = 30 * 1000;

        const databaseUrl = "mongodb://127.0.0.1/sep";
        const  options = {
                connectTimeoutMS: timeout,
                keepAlive: timeout,
                useCreateIndex: true,
                useNewUrlParser: true,
                useUnifiedTopology: true,
                useFindAndModify: false,
            };
        return await mongoose.connect(databaseUrl, options);
    })();

    mongoose.set("debug", true);

    mongoose.connection.on("error", (err) => {
        console.error("MongoDB connection: error - " + err);
    });

    mongoose.connection.on("connected", () => {
        console.info("MongoDB connection: connected");
    });

    mongoose.connection.on("open", () => {
        console.info("MongoDB connection: open");
    });

    mongoose.connection.on("reconnected", () => {
        console.info("MongoDB connection: reconnected");
    });

    mongoose.connection.on("disconnected", () => {
        console.warn("MongoDB connection: disconnected");
    });

    process.on("SIGINT", () => {
        mongoose.disconnect(() => {
            process.exit(0);
        });
    });

    return mongoose;
})();
