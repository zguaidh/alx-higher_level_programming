#!/usr/bin/node
/* global $ */
/* JavaScript script that updates the text of the <header>
  when the user clicks on DIV#update_header
 */
$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
