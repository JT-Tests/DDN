const {
	BAD_REQUEST_CODE,
	UNAUTHORIZED_CODE,
	FORBIDDEN_CODE,
	NOT_FOUND_CODE,
	CONFLICT_CODE,
	GONE_CODE,
	UNSUPPORTED_MEDIA_TYPE_CODE,
	VALIDATION_ERROR_CODE,
	SERVER_ERROR_CODE,
	SERVICE_UNAVAILABLE_CODE,
} = require("../constants/statusCodes");

class GeneralError extends Error {
	constructor(message) {
		super();
		this.message = message;
	}

	getCode() {
		if (this instanceof BadRequest) return BAD_REQUEST_CODE;
		if (this instanceof AuthError) return UNAUTHORIZED_CODE;
		if (this instanceof Forbidden) return FORBIDDEN_CODE;
		if (this instanceof NotFound) return NOT_FOUND_CODE;
		if (this instanceof Conflict) return CONFLICT_CODE;
		if (this instanceof Gone) return GONE_CODE;
		if (this instanceof UnsupportedMediaType) return UNSUPPORTED_MEDIA_TYPE_CODE;
		if (this instanceof ValidationError) return VALIDATION_ERROR_CODE;
		if (this instanceof ExternalApiError) return SERVICE_UNAVAILABLE_CODE;

		return SERVER_ERROR_CODE;
	}
}

class BadRequest extends GeneralError {}
class AuthError extends GeneralError {}
class Forbidden extends GeneralError {}
class NotFound extends GeneralError {}
class Conflict extends GeneralError {}
class Gone extends GeneralError {}
class UnsupportedMediaType extends GeneralError {}
class ValidationError extends GeneralError {}
class ExternalApiError extends GeneralError {}

module.exports = {
	GeneralError,
	BadRequest,
	AuthError,
	Forbidden,
	NotFound,
	Conflict,
	Gone,
	UnsupportedMediaType,
	ValidationError,
	ExternalApiError,
};
