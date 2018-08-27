function RunestoneBase () {   // Basic parent stuff

}

RunestoneBase.prototype.logEvents = false;

RunestoneBase.prototype.logBookEvent = function (eventInfo) {

    if (!this.logEvents)
        return;

    eventInfo.course = eBookConfig.course;
    if (eBookConfig.useRunestoneServices && eBookConfig.logLevel > 0) {
        jQuery.get(eBookConfig.ajaxURL + 'hsblog', eventInfo); // Log the run event
    }
    console.log("logging event " + eventInfo);
};

RunestoneBase.prototype.logRunEvent = function (eventInfo) {

    if (!this.logEvents)
        return;

    eventInfo.course = eBookConfig.course;
    if (eBookConfig.useRunestoneServices && eBookConfig.logLevel > 0) {
        jQuery.post(eBookConfig.ajaxURL + 'runlog', eventInfo); // Log the run event
    }
    console.log("running " + eventInfo);
};

