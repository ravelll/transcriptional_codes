import React from "react";
import ReactDOM from "react-dom";
import TaskApp from "./TaskApp";

$(function () {
    ReactDOM.render(
      <TaskApp />,
      document.getElementsByName('container')
    );
});
