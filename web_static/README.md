# HTML (Hypertext Markup Language)

HTML is the standard markup language used to create and design web pages. It consists of a set of tags and attributes that define the structure and content of a webpage.

## How to Create an HTML Page

To create an HTML page, follow these steps:

1. Open a text editor like Notepad, Visual Studio Code, or Sublime Text.
2. Begin with the HTML document structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Title</title>
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>
```

3. Add content within the `<body>` tags using various HTML elements.

## Markup Language

A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. It describes the structure of the document and includes elements to define headings, paragraphs, lists, links, images, and more.

## DOM (Document Object Model)

The Document Object Model is a programming interface for web documents. It represents the structure of HTML and XML documents as a tree-like structure, where each node represents an object.

## Element / Tag

An element or tag is a fundamental building block of HTML. It consists of a start tag, content, and an end tag (in most cases). Elements define the structure and semantics of a webpage.

Example:
```html
<p>This is a paragraph element.</p>
```

In this example, `<p>` is the start tag, `This is a paragraph element.` is the content, and `</p>` is the end tag.

## Attribute

Attributes provide additional information about an HTML element and are defined within the start tag. Attributes consist of a name and a value.

Example:
```html
<a href="https://example.com">Click here</a>
```

In this example, `href` is the attribute name, and `"https://example.com"` is the attribute value.

## Browser Loading Process

When a browser loads a webpage, it follows these general steps:

1. **HTML Parsing**: The browser retrieves the HTML file from the server.
2. **DOM Construction**: The browser parses the HTML and constructs the Document Object Model (DOM) tree.
3. **Render Tree Construction**: The browser computes the CSS styles and constructs the render tree.
4. **Layout**: The browser calculates the position and size of each element on the page.
5. **Painting**: The browser paints the content on the screen.

## CSS (Cascading Style Sheets)

CSS is a stylesheet language used to control the presentation and layout of HTML documents. It allows you to define styles for elements, including colors, fonts, spacing, and more.

## Adding Style to an Element

You can add style to an HTML element using inline styles or by linking an external CSS file.

Example of inline style:
```html
<p style="color: blue; font-size: 16px;">This is a styled paragraph.</p>
```

Example of external CSS:
```html
<head>
    <link rel="stylesheet" href="styles.css">
</head>
```

## Class

A class is a way to apply a set of styles to multiple elements. You define a class in CSS and then apply it to HTML elements using the `class` attribute.

Example:
```css
.myClass {
    color: red;
    font-size: 18px;
}
```

```html
<p class="myClass">This paragraph has the "myClass" style applied.</p>
```

## Selector

A selector is a pattern used to select HTML elements to which styles should be applied. Selectors can target elements based on their tag name, class, ID, attributes, and more.

Example of class selector:
```css
.myClass {
    color: red;
}
```

## CSS Specificity

CSS specificity is a set of rules that determine which CSS styles should be applied to an element when multiple conflicting styles exist. Specificity is calculated based on the type of selector used.

To compute CSS specificity:

1. Count the number of ID selectors.
2. Count the number of class selectors, attributes selectors, and pseudo-classes.
3. Count the number of element selectors and pseudo-elements.

The style with the highest specificity will be applied to the element.

Example:
```css
/* Specificity: 0-0-1 */
p {
    color: blue;
}

/* Specificity: 0-1-0 */
.myClass {
    color: red;
}

/* Specificity: 1-0-0 */
#uniqueID {
    color: green;
}
```