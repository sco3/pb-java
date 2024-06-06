/*eslint-disable block-scoped-var, id-length, no-control-regex, no-magic-numbers, no-prototype-builtins, no-redeclare, no-shadow, no-var, sort-vars*/
(function(global, factory) { /* global define, require, module */

    /* AMD */ if (typeof define === 'function' && define.amd)
        define(["protobufjs/minimal"], factory);

    /* CommonJS */ else if (typeof require === 'function' && typeof module === 'object' && module && module.exports)
        module.exports = factory(require("protobufjs/minimal"));

})(this, function($protobuf) {
    "use strict";

    // Common aliases
    var $Reader = $protobuf.Reader, $Writer = $protobuf.Writer, $util = $protobuf.util;
    
    // Exported root namespace
    var $root = $protobuf.roots["default"] || ($protobuf.roots["default"] = {});
    
    $root.sco3 = (function() {
    
        /**
         * Namespace sco3.
         * @exports sco3
         * @namespace
         */
        var sco3 = {};
    
        sco3.Hello = (function() {
    
            /**
             * Properties of a Hello.
             * @memberof sco3
             * @interface IHello
             * @property {string|null} [name] Hello name
             */
    
            /**
             * Constructs a new Hello.
             * @memberof sco3
             * @classdesc Represents a Hello.
             * @implements IHello
             * @constructor
             * @param {sco3.IHello=} [properties] Properties to set
             */
            function Hello(properties) {
                if (properties)
                    for (var keys = Object.keys(properties), i = 0; i < keys.length; ++i)
                        if (properties[keys[i]] != null)
                            this[keys[i]] = properties[keys[i]];
            }
    
            /**
             * Hello name.
             * @member {string} name
             * @memberof sco3.Hello
             * @instance
             */
            Hello.prototype.name = "";
    
            /**
             * Creates a new Hello instance using the specified properties.
             * @function create
             * @memberof sco3.Hello
             * @static
             * @param {sco3.IHello=} [properties] Properties to set
             * @returns {sco3.Hello} Hello instance
             */
            Hello.create = function create(properties) {
                return new Hello(properties);
            };
    
            /**
             * Encodes the specified Hello message. Does not implicitly {@link sco3.Hello.verify|verify} messages.
             * @function encode
             * @memberof sco3.Hello
             * @static
             * @param {sco3.IHello} message Hello message or plain object to encode
             * @param {$protobuf.Writer} [writer] Writer to encode to
             * @returns {$protobuf.Writer} Writer
             */
            Hello.encode = function encode(message, writer) {
                if (!writer)
                    writer = $Writer.create();
                if (message.name != null && Object.hasOwnProperty.call(message, "name"))
                    writer.uint32(/* id 1, wireType 2 =*/10).string(message.name);
                return writer;
            };
    
            /**
             * Encodes the specified Hello message, length delimited. Does not implicitly {@link sco3.Hello.verify|verify} messages.
             * @function encodeDelimited
             * @memberof sco3.Hello
             * @static
             * @param {sco3.IHello} message Hello message or plain object to encode
             * @param {$protobuf.Writer} [writer] Writer to encode to
             * @returns {$protobuf.Writer} Writer
             */
            Hello.encodeDelimited = function encodeDelimited(message, writer) {
                return this.encode(message, writer).ldelim();
            };
    
            /**
             * Decodes a Hello message from the specified reader or buffer.
             * @function decode
             * @memberof sco3.Hello
             * @static
             * @param {$protobuf.Reader|Uint8Array} reader Reader or buffer to decode from
             * @param {number} [length] Message length if known beforehand
             * @returns {sco3.Hello} Hello
             * @throws {Error} If the payload is not a reader or valid buffer
             * @throws {$protobuf.util.ProtocolError} If required fields are missing
             */
            Hello.decode = function decode(reader, length) {
                if (!(reader instanceof $Reader))
                    reader = $Reader.create(reader);
                var end = length === undefined ? reader.len : reader.pos + length, message = new $root.sco3.Hello();
                while (reader.pos < end) {
                    var tag = reader.uint32();
                    switch (tag >>> 3) {
                    case 1: {
                            message.name = reader.string();
                            break;
                        }
                    default:
                        reader.skipType(tag & 7);
                        break;
                    }
                }
                return message;
            };
    
            /**
             * Decodes a Hello message from the specified reader or buffer, length delimited.
             * @function decodeDelimited
             * @memberof sco3.Hello
             * @static
             * @param {$protobuf.Reader|Uint8Array} reader Reader or buffer to decode from
             * @returns {sco3.Hello} Hello
             * @throws {Error} If the payload is not a reader or valid buffer
             * @throws {$protobuf.util.ProtocolError} If required fields are missing
             */
            Hello.decodeDelimited = function decodeDelimited(reader) {
                if (!(reader instanceof $Reader))
                    reader = new $Reader(reader);
                return this.decode(reader, reader.uint32());
            };
    
            /**
             * Verifies a Hello message.
             * @function verify
             * @memberof sco3.Hello
             * @static
             * @param {Object.<string,*>} message Plain object to verify
             * @returns {string|null} `null` if valid, otherwise the reason why it is not
             */
            Hello.verify = function verify(message) {
                if (typeof message !== "object" || message === null)
                    return "object expected";
                if (message.name != null && message.hasOwnProperty("name"))
                    if (!$util.isString(message.name))
                        return "name: string expected";
                return null;
            };
    
            /**
             * Creates a Hello message from a plain object. Also converts values to their respective internal types.
             * @function fromObject
             * @memberof sco3.Hello
             * @static
             * @param {Object.<string,*>} object Plain object
             * @returns {sco3.Hello} Hello
             */
            Hello.fromObject = function fromObject(object) {
                if (object instanceof $root.sco3.Hello)
                    return object;
                var message = new $root.sco3.Hello();
                if (object.name != null)
                    message.name = String(object.name);
                return message;
            };
    
            /**
             * Creates a plain object from a Hello message. Also converts values to other types if specified.
             * @function toObject
             * @memberof sco3.Hello
             * @static
             * @param {sco3.Hello} message Hello
             * @param {$protobuf.IConversionOptions} [options] Conversion options
             * @returns {Object.<string,*>} Plain object
             */
            Hello.toObject = function toObject(message, options) {
                if (!options)
                    options = {};
                var object = {};
                if (options.defaults)
                    object.name = "";
                if (message.name != null && message.hasOwnProperty("name"))
                    object.name = message.name;
                return object;
            };
    
            /**
             * Converts this Hello to JSON.
             * @function toJSON
             * @memberof sco3.Hello
             * @instance
             * @returns {Object.<string,*>} JSON object
             */
            Hello.prototype.toJSON = function toJSON() {
                return this.constructor.toObject(this, $protobuf.util.toJSONOptions);
            };
    
            /**
             * Gets the default type url for Hello
             * @function getTypeUrl
             * @memberof sco3.Hello
             * @static
             * @param {string} [typeUrlPrefix] your custom typeUrlPrefix(default "type.googleapis.com")
             * @returns {string} The default type url
             */
            Hello.getTypeUrl = function getTypeUrl(typeUrlPrefix) {
                if (typeUrlPrefix === undefined) {
                    typeUrlPrefix = "type.googleapis.com";
                }
                return typeUrlPrefix + "/sco3.Hello";
            };
    
            return Hello;
        })();
    
        return sco3;
    })();

    return $root;
});
