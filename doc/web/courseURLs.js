// Returns true if the current page is within an iFrame.
function inIframe () {
    try {
        return window.self !== window.top;
    } catch (e) {
        return true;
    }
}

// course-specific URL
var courseURL = "https://chalmers.instructure.com/courses/15292/";

// Course-specific url if the current page is within an iFrame.
// Relative link to file if the current page is the top window
var kursmaterial = "";
if (inIframe()) {
	kursmaterial = courseURL + "external_tools/743";
} else {
	kursmaterial = 'material.html';
}

var syllabus = "";
if (inIframe()) {
	syllabus = courseURL + "assignments/syllabus";
} else {
	syllabus = 'syllabus2021.html';
}

var veckoplanering = "";
if (inIframe()) {
	veckoplanering = courseURL + "external_tools/741";
} else {
	veckoplanering = 'schedule.html';
}

var distansundervisning = "";
if (inIframe()) {
	distansundervisning = courseURL + "external_tools/602";
} else {
	distansundervisning = 'distansundervisning.html';
}

var datorlab1 = "https://chalmers.instructure.com/courses/15292/assignments/19703";

var datorlab2 = "https://chalmers.instructure.com/courses/15292/assignments/19704";

