<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <title>${self.title()}</title>
        ${self.meta()}
		${self.css()}
        ${self.javascript()}
	</head>
    <body>
        <script type="text/javascript">
        $(document).ready(function(){
            ${self.docready()}
        });
        </script>
		${next.body()}
    </body>
</html>

<%def name="title()">
	py-denon console
</%def>

<%def name="docready()"></%def>
<%def name="css()">
<%include file="/ui/layout/iphone/css.mako"/>
</%def>
<%def name="javascript()">
<%include file="/ui/layout/iphone/javascript.mako"/>
</%def>
<%def name="meta()">
    <meta name="viewport" content="width=320" />
</%def>