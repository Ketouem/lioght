from flask import jsonify, request, g, current_app, Response

from . import api


@api.route("/provider", methods=["GET"])
def get_provider():
    return jsonify(provider=current_app.config["LIGHT_PROVIDER"])


@api.route("/lights/<int:lid>/color", methods=["POST"])
def set_color(lid):
    params = request.json
    red = params.get("red")
    green = params.get("green")
    blue = params.get("blue")
    color = "#{}{}{}".format(red, green, blue)
    current_app.logger.debug("Changing {} to {}".format(lid, color))
    current_app.logger.debug(g.controller._milight._hosts)
    g.controller.change_color(lid, color)
    return Response(status=200)


@api.route("/lights/<int:lid>/on", methods=['POST'])
def switch_on(lid):
    g.controller.switch_on(lid)
    return Response(status=200)


@api.route("/lights/<int:lid>/off", methods=['POST'])
def switch_off(lid):
    g.controller.switch_off(lid)
    return Response(status=200)


@api.route("/lights/on", methods=["POST"])
def switch_all_on():
    g.controller.switch_all_on()
    return Response(status=200)


@api.route("/lights/off", methods=["POST"])
def switch_all_off():
    g.controller.switch_all_off()
    return Response(status=200)
