


# 📘 Part 1 – Global Components Mapping

**Project:** Varhadi Virasat Restaurant Management System

---

## 1. Global Components Overview

| Component          | HTML File(s) | CSS File    | JavaScript  | Purpose                          |
| ------------------ | ------------ | ----------- | ----------- | -------------------------------- |
| Navbar             | `base.html`  | `style.css` | `script.js` | Main navigation across all pages |
| Footer             | `base.html`  | `style.css` | —           | Website footer                   |
| Preloader          | `base.html`  | `style.css` | `script.js` | Loading animation                |
| Toast Notification | `base.html`  | `style.css` | `script.js` | Success/error notifications      |
| Scroll To Top      | `base.html`  | `style.css` | `script.js` | Scroll back to top               |
| WhatsApp Button    | `base.html`  | `style.css` | —           | Quick WhatsApp contact           |

---

# 2. Navbar Mapping

| Selector            | HTML File   | Purpose                   | Used By JS |
| ------------------- | ----------- | ------------------------- | ---------- |
| `.navbar`           | `base.html` | Main navigation container | ✅          |
| `.logo`             | `base.html` | Restaurant logo           | ❌          |
| `.logo-text`        | `base.html` | Restaurant name           | ❌          |
| `.nav-links`        | `base.html` | Navigation menu           | ✅          |
| `.nav-links.active` | `base.html` | Mobile menu state         | ✅          |
| `.menu-toggle`      | `base.html` | Hamburger menu            | ✅          |
| `.navbar-scrolled`  | `base.html` | Navbar after scrolling    | ✅          |
| `.cart-link`        | `base.html` | Cart navigation           | ❌          |
| `#cart-count`       | `base.html` | Cart item count           | ✅          |

### JavaScript Functions

| Function             | Selectors Used                |
| -------------------- | ----------------------------- |
| Mobile Menu Toggle   | `.menu-toggle`, `.nav-links`  |
| Navbar Scroll Effect | `.navbar`, `.navbar-scrolled` |
| Cart Counter Update  | `#cart-count`                 |

---

# 3. Footer Mapping

| Selector         | HTML        | Purpose            |
| ---------------- | ----------- | ------------------ |
| `.footer`        | `base.html` | Main footer        |
| `.footer-grid`   | `base.html` | Footer columns     |
| `.footer-column` | `base.html` | Footer sections    |
| `.footer-bottom` | `base.html` | Copyright area     |
| `.social-links`  | `base.html` | Social media icons |

---

# 4. Preloader

| Selector       | HTML        | Purpose           | JS |
| -------------- | ----------- | ----------------- | -- |
| `#preloader`   | `base.html` | Loader overlay    | ✅  |
| `.loader-box`  | `base.html` | Loading animation | ❌  |
| `.loader-text` | `base.html` | Loading text      | ❌  |

### JavaScript

| Function       | Purpose                        |
| -------------- | ------------------------------ |
| Hide Preloader | Removes loader after page load |

---

# 5. Toast Notification

| Selector      | HTML        | Purpose                | JS |
| ------------- | ----------- | ---------------------- | -- |
| `.toast`      | `base.html` | Notification container | ✅  |
| `.toast.show` | `base.html` | Display animation      | ✅  |

### Used By

* Add to Cart
* Remove Item
* Order Success
* Reservation Status
* Admin Messages

---

# 6. Scroll To Top

| Selector        | HTML        | Purpose       | JS |
| --------------- | ----------- | ------------- | -- |
| `#scrollTopBtn` | `base.html` | Scroll button | ✅  |

### JavaScript

| Function         | Purpose                 |
| ---------------- | ----------------------- |
| Show/Hide Button | Appears while scrolling |
| Scroll To Top    | Smooth scroll to top    |

---

# 7. WhatsApp Floating Button

| Selector          | HTML        | Purpose                | JS |
| ----------------- | ----------- | ---------------------- | -- |
| `.whatsapp-float` | `base.html` | Floating WhatsApp icon | ❌  |

---

# 8. Global Animation Classes

| Selector   | Used In        | Purpose            |
| ---------- | -------------- | ------------------ |
| `.fade-in` | Multiple Pages | Fade animation     |
| `.reveal`  | Home/Menu      | Scroll reveal      |
| `.active`  | Navbar/Menu    | Active state       |
| `:hover`   | Global         | Hover effects      |
| `::before` | Global         | Decorative styling |
| `::after`  | Global         | Decorative styling |

---

# 9. Global Dependency Map

```text
base.html
│
├── Navbar
│   ├── .navbar
│   ├── .logo
│   ├── .logo-text
│   ├── .nav-links
│   ├── .menu-toggle
│   └── #cart-count
│
├── Page Content
│
├── Toast
│   └── .toast
│
├── Preloader
│   ├── #preloader
│   ├── .loader-box
│   └── .loader-text
│
├── WhatsApp
│   └── .whatsapp-float
│
├── Scroll Top
│   └── #scrollTopBtn
│
└── Footer
    ├── .footer
    ├── .footer-grid
    ├── .footer-column
    └── .footer-bottom
```

---

## 📊 Part 1 Summary

| Item                  |           Count |
| --------------------- | --------------: |
| Global Components     |               6 |
| CSS Selectors Covered |             25+ |
| JavaScript Functions  |               6 |
| HTML Files            | 1 (`base.html`) |
| CSS Files             | 1 (`style.css`) |
| JS Files              | 1 (`script.js`) |

---

=========================================================================================================


# 🏠 HOME PAGE (`index.html`)

| Section No. | Section         | Main Classes                                                             | JS Used | Responsive |
| ----------: | --------------- | ------------------------------------------------------------------------ | ------- | :--------: |
|         2.1 | Hero            | `.hero`, `.hero-container`, `.hero-left`, `.hero-title`, `.hero-buttons` | ✅       |      ✅     |
|         2.2 | Highlights      | `.highlights`, `.highlight-card`                                         | ❌       |      ✅     |
|         2.3 | Counter         | `.counter-section`, `.counter-box`                                       | ✅       |      ✅     |
|         2.4 | Categories      | `.home-categories`, `.home-category-grid`, `.home-category-card`         | ❌       |      ✅     |
|         2.5 | Chef Special    | `.chef-special`, `.premium-menu-grid`, `.premium-card`                   | ✅       |      ✅     |
|         2.6 | Why Choose Us   | `.why-modern`, `.why-modern-grid`, `.why-modern-card`                    | ❌       |      ✅     |
|         2.7 | Gallery         | `.gallery-section`, `.gallery-grid`, `.gallery-item`                     | ✅       |      ✅     |
|         2.8 | Reservation CTA | `.reservation-home`, `.reservation-box`, `.reservation-btn`              | ❌       |      ✅     |
|         2.9 | Testimonials    | `.testimonials`, `.testimonial-slider`, `.testimonial`                   | ✅       |      ✅     |

---

## Documentation Format for Each Section

For every section, you'll get:

### Example: Hero Section

| Selector          | HTML Element | Purpose           | JS Function    | Responsive |
| ----------------- | ------------ | ----------------- | -------------- | :--------: |
| `.hero`           | `<section>`  | Hero container    | Hero animation |      ✅     |
| `.hero-container` | `<div>`      | Two-column layout | —              |      ✅     |
| `.hero-title`     | `<h1>`       | Main heading      | Text animation |      ✅     |
| `.hero-subtitle`  | `<p>`        | Subtitle          | —              |      ✅     |
| `.hero-buttons`   | `<div>`      | CTA buttons       | Button click   |      ✅     |

Then you'll receive:

* **HTML hierarchy**
* **CSS dependency**
* **JavaScript interaction**
* **Responsive behavior**
* **Animation flow**
* **Section dependency map**

---

=========================================================================================================


### 📘 Part 2 – Home Page (`index.html`)

1. **Hero Section**

   * HTML structure
   * CSS selectors
   * JavaScript interactions
   * Responsive behavior
   * Dependency map

2. **Highlights Section**

   * Complete selector mapping
   * Card layout
   * Hover effects

3. **Counter Section**

   * Counter cards
   * Animation
   * JavaScript mapping

4. **Home Categories**

   * Grid system
   * Category cards
   * Navigation links

5. **Chef Special**

   * Premium menu cards
   * Ratings
   * Add-to-cart button
   * Badges

6. **Why Choose Us**

   * Feature cards
   * Icons
   * Grid layout

7. **Gallery**

   * Gallery grid
   * Lightbox
   * Image animations

8. **Reservation CTA**

   * Background overlay
   * CTA button
   * Call-to-action layout

9. **Testimonials**

   * Testimonial cards
   * Slider
   * Dots navigation

10. **Complete Home Dependency Map**

    * HTML → CSS
    * CSS → JS
    * Section hierarchy

---

## 📑 Final Deliverable

After all parts are completed, you'll have a document like this:

```text
Restaurant Management System Documentation
│
├── Part 1 : Global Components
├── Part 2 : Home Page
├── Part 3 : Menu Page
├── Part 4 : Cart & Checkout
├── Part 5 : Reservation & Invoice
├── Part 6 : Admin Panel
├── Part 7 : JavaScript Mapping
├── Part 8 : CSS Selector Index
├── Part 9 : HTML Component Map
└── Part 10 : Complete Project Dependency Map
```

The finished documentation will serve as a **developer reference manual**, making it easy to:

* Find where any class or selector is used.
* Understand the relationship between HTML, CSS, and JavaScript.
* Explain your project confidently during your viva.
* Maintain or extend the project in the future.


=====================================================================================================



Each section will include:

| Field         | Description                                   |
| ------------- | --------------------------------------------- |
| HTML File     | Where the section is defined                  |
| CSS Selectors | All classes/IDs used                          |
| JavaScript    | Functions/events interacting with the section |
| Purpose       | What each selector does                       |
| Responsive    | Desktop / Tablet / Mobile behavior            |
| Dependencies  | HTML ↔ CSS ↔ JS relationships                 |

For example:

| Selector          | HTML Element | Purpose           | JS Interaction | Responsive |
| ----------------- | ------------ | ----------------- | -------------- | :--------: |
| `.hero`           | `<section>`  | Hero container    | Hero animation |      ✅     |
| `.hero-container` | `<div>`      | Two-column layout | —              |      ✅     |
| `.hero-title`     | `<h1>`       | Main title        | Text animation |      ✅     |
| `.hero-buttons`   | `<div>`      | CTA buttons       | Click handlers |      ✅     |


=======================================================================================================


# 📘 Part 2.1 – Home Page → Hero Section (`index.html`)

---

# 2.1 Hero Overview

| Property            | Details                         |
| ------------------- | ------------------------------- |
| **HTML File**       | `index.html`                    |
| **CSS File**        | `style.css`                     |
| **JavaScript File** | `script.js`                     |
| **Section Type**    | Landing / Hero                  |
| **Responsive**      | ✅ Desktop • ✅ Tablet • ✅ Mobile |
| **Animation**       | Background, Reveal, Buttons     |

---

# Hero Structure

```text
Hero Section
│
├── Hero Background
│   ├── hero-bg
│   ├── hero-bg-1
│   ├── hero-bg-2
│   └── hero-overlay
│
├── Hero Container
│   │
│   ├── Left Side
│   │   ├── hero-badge
│   │   ├── hero-marathi
│   │   ├── hero-title
│   │   ├── hero-subtitle
│   │   ├── hero-description
│   │   └── hero-buttons
│   │
│   └── Right Side
│       └── Hero Image
│
└── Hero Scroll
```

---

# CSS Mapping

| Selector            | HTML Element   | Purpose               | JS Used | Responsive |
| ------------------- | -------------- | --------------------- | :-----: | :--------: |
| `.hero`             | `<section>`    | Main Hero container   |    ❌    |      ✅     |
| `.hero-bg`          | `<div>`        | Background wrapper    |    ❌    |      ✅     |
| `.hero-bg-1`        | `<div>`        | Background image 1    |    ✅    |      ✅     |
| `.hero-bg-2`        | `<div>`        | Background image 2    |    ✅    |      ✅     |
| `.hero-overlay`     | `<div>`        | Dark overlay          |    ❌    |      ✅     |
| `.hero-container`   | `<div>`        | Main layout container |    ❌    |      ✅     |
| `.hero-left`        | `<div>`        | Left content          |    ❌    |      ✅     |
| `.hero-badge`       | `<span>`       | Restaurant badge      |    ❌    |      ✅     |
| `.hero-marathi`     | `<p>`          | Marathi slogan        |    ❌    |      ✅     |
| `.hero-title`       | `<h1>`         | Main heading          |    ❌    |      ✅     |
| `.hero-subtitle`    | `<h3>`         | Secondary heading     |    ❌    |      ✅     |
| `.hero-description` | `<p>`          | Description           |    ❌    |      ✅     |
| `.hero-buttons`     | `<div>`        | CTA button wrapper    |    ❌    |      ✅     |
| `.hero-btn`         | `<a>/<button>` | Call-to-action button |    ✅    |      ✅     |
| `.hero-scroll`      | `<div>`        | Scroll indicator      |    ✅    |      ✅     |

---

# HTML Hierarchy

```text
section.hero
│
├── div.hero-bg
│   ├── div.hero-bg-1
│   ├── div.hero-bg-2
│   └── div.hero-overlay
│
├── div.hero-container
│
│   ├── div.hero-left
│   │
│   ├── span.hero-badge
│   ├── p.hero-marathi
│   ├── h1.hero-title
│   ├── h3.hero-subtitle
│   ├── p.hero-description
│   │
│   └── div.hero-buttons
│       ├── a.hero-btn
│       └── a.hero-btn
│
└── div.hero-scroll
```

---

# JavaScript Interaction

| Function                  | Uses                       | Purpose                        |
| ------------------------- | -------------------------- | ------------------------------ |
| Hero Background Animation | `.hero-bg-1`, `.hero-bg-2` | Rotates/Fades hero backgrounds |
| Button Click              | `.hero-btn`                | Navigate to Menu/Reservation   |
| Scroll Animation          | `.hero-scroll`             | Scroll to next section         |

---

# Responsive Behavior

| Device  | Layout                       |
| ------- | ---------------------------- |
| Desktop | Two-column Hero              |
| Tablet  | Compact two-column           |
| Mobile  | Single-column stacked layout |

---

# Visual Flow

```text
Visitor Opens Website
        │
        ▼
Hero Background Loads
        │
        ▼
Overlay Applied
        │
        ▼
Hero Content Appears
        │
        ▼
Buttons Become Clickable
        │
        ▼
Scroll Indicator Guides User
```

---

# Dependencies

```text
index.html
     │
     ▼
Hero HTML
     │
     ▼
style.css
     │
     ├── Layout
     ├── Typography
     ├── Background
     ├── Buttons
     └── Responsive Rules
     │
     ▼
script.js
     │
     ├── Background Animation
     ├── Button Actions
     └── Scroll Animation
```

---

# Hero Section Summary

| Item                    | Count |
| ----------------------- | ----: |
| HTML Elements           |   ~14 |
| CSS Selectors           |    14 |
| JavaScript Interactions |     3 |
| Responsive Breakpoints  |     3 |
| Animation Effects       |     3 |

---

=======================================================================================================

---

# 📘 Part 2.2 – Home Page → Highlights Section (`index.html`)

---

# 2.2 Highlights Overview

| Property            | Details                         |
| ------------------- | ------------------------------- |
| **HTML File**       | `index.html`                    |
| **CSS File**        | `style.css`                     |
| **JavaScript File** | `script.js`                     |
| **Section Type**    | Feature Highlights              |
| **Responsive**      | ✅ Desktop • ✅ Tablet • ✅ Mobile |
| **Animation**       | Hover Effect / Scroll Reveal    |

---

# Section Purpose

The **Highlights** section showcases the restaurant's key strengths (such as Fresh Ingredients, Fast Service, Hygienic Kitchen, Authentic Taste) using icon cards.

---

# Structure

```text
Highlights Section
│
└── highlights
    │
    ├── highlight-card
    │     ├── icon
    │     ├── title
    │     └── description
    │
    ├── highlight-card
    │
    ├── highlight-card
    │
    └── highlight-card
```

---

# CSS Mapping

| Selector                | HTML Element | Purpose                 | JS Used | Responsive |
| ----------------------- | ------------ | ----------------------- | :-----: | :--------: |
| `.highlights`           | `<section>`  | Main highlights section |    ❌    |      ✅     |
| `.highlight-card`       | `<div>`      | Individual feature card |    ❌    |      ✅     |
| `.highlight-card i`     | `<i>`        | Feature icon            |    ❌    |      ✅     |
| `.highlight-card h3`    | `<h3>`       | Feature title           |    ❌    |      ✅     |
| `.highlight-card p`     | `<p>`        | Feature description     |    ❌    |      ✅     |
| `.highlight-card:hover` | CSS          | Hover animation         |    ❌    |      ✅     |

---

# HTML Hierarchy

```text
section.highlights
│
├── div.highlight-card
│      ├── i
│      ├── h3
│      └── p
│
├── div.highlight-card
│
├── div.highlight-card
│
└── div.highlight-card
```

---

# JavaScript Interaction

| Function                         | Selector                | Purpose                 |
| -------------------------------- | ----------------------- | ----------------------- |
| Scroll Reveal *(if implemented)* | `.highlight-card`       | Animate cards into view |
| Hover Effect                     | `.highlight-card:hover` | CSS-driven animation    |

> **Note:** Based on the project structure, this section is primarily styled with CSS. If your `script.js` does not explicitly manipulate `.highlight-card`, then there is **no direct JavaScript dependency**.

---

# Responsive Layout

| Screen Size | Layout           |
| ----------- | ---------------- |
| Desktop     | 4 cards in a row |
| Tablet      | 2 cards per row  |
| Mobile      | 1 card per row   |

---

# Visual Flow

```text
Page Loads
     │
     ▼
Highlights Section Appears
     │
     ▼
Feature Cards Display
     │
     ▼
User Hovers Card
     │
     ▼
Card Elevates / Shadow Changes
```

---

# Dependency Map

```text
index.html
     │
     ▼
.highlights
     │
     ├── .highlight-card
     │      ├── Icon
     │      ├── Title
     │      └── Description
     │
     ▼
style.css
     │
     ├── Grid Layout
     ├── Card Design
     ├── Hover Effect
     └── Responsive Rules
```

---

# Highlights Summary

| Item                   |                                    Count |
| ---------------------- | ---------------------------------------: |
| Main Section           |                                        1 |
| Feature Cards          |                                        4 |
| CSS Selectors          |                                        6 |
| JavaScript Functions   | 0–1 (depending on reveal implementation) |
| Responsive Breakpoints |                                        3 |
| Hover Effects          |                                        1 |

---

=======================================================================================================


# 📘 Part 2.3 – Home Page → Counter Section (`index.html`)

---

# 2.3 Counter Overview

| Property            | Details                          |
| ------------------- | -------------------------------- |
| **HTML File**       | `index.html`                     |
| **CSS File**        | `style.css`                      |
| **JavaScript File** | `script.js`                      |
| **Section Type**    | Statistics / Achievement Counter |
| **Responsive**      | ✅ Desktop • ✅ Tablet • ✅ Mobile  |
| **Animation**       | Counter Animation, Scroll Reveal |

---

# Section Purpose

The **Counter Section** displays the restaurant's achievements using animated statistic cards.

Typical information displayed includes:

* Happy Customers
* Delicious Dishes
* Expert Chefs
* Years of Experience

---

# Structure

```text
Counter Section
│
└── counter-section
      │
      ├── counter-box
      │      ├── counter-icon
      │      ├── counter-number
      │      └── counter-title
      │
      ├── counter-box
      ├── counter-box
      └── counter-box
```

---

# CSS Mapping

| Selector             | HTML Element      | Purpose                 | JS Used | Responsive |
| -------------------- | ----------------- | ----------------------- | :-----: | :--------: |
| `.counter-section`   | `<section>`       | Counter container       |    ❌    |      ✅     |
| `.counter-container` | `<div>`           | Grid/Flex wrapper       |    ❌    |      ✅     |
| `.counter-box`       | `<div>`           | Individual counter card |    ✅    |      ✅     |
| `.counter-icon`      | `<i>` / `<img>`   | Counter icon            |    ❌    |      ✅     |
| `.counter-number`    | `<h2>` / `<span>` | Animated number         |    ✅    |      ✅     |
| `.counter-title`     | `<p>`             | Counter label           |    ❌    |      ✅     |
| `.counter-box:hover` | CSS               | Hover animation         |    ❌    |      ✅     |

---

# HTML Hierarchy

```text
section.counter-section
│
└── div.counter-container
      │
      ├── div.counter-box
      │      ├── i.counter-icon
      │      ├── h2.counter-number
      │      └── p.counter-title
      │
      ├── div.counter-box
      ├── div.counter-box
      └── div.counter-box
```

---

# JavaScript Interaction

| Function                         | Selector          | Purpose                                    |
| -------------------------------- | ----------------- | ------------------------------------------ |
| Counter Animation                | `.counter-number` | Animates numbers from 0 to target value    |
| Scroll Reveal *(if implemented)* | `.counter-box`    | Reveals cards when section enters viewport |

---

# Responsive Layout

| Device  | Layout                |
| ------- | --------------------- |
| Desktop | 4 counters in one row |
| Tablet  | 2 × 2 grid            |
| Mobile  | Single-column stack   |

---

# Visual Flow

```text
Page Scroll
     │
     ▼
Counter Section Visible
     │
     ▼
Animation Starts
     │
     ▼
Numbers Count Up
     │
     ▼
Animation Stops at Target Value
```

---

# Dependency Map

```text
index.html
     │
     ▼
.counter-section
     │
     ├── .counter-container
     │
     ├── .counter-box
     │      ├── .counter-icon
     │      ├── .counter-number
     │      └── .counter-title
     │
     ▼
style.css
     │
     ├── Grid Layout
     ├── Card Styling
     ├── Hover Effects
     └── Responsive Rules
     │
     ▼
script.js
     │
     ├── Counter Animation
     └── Scroll Trigger
```

---

# User Interaction Flow

```text
User Opens Home Page
          │
          ▼
Scrolls Down
          │
          ▼
Counter Section Appears
          │
          ▼
Numbers Animate
          │
          ▼
User Sees Restaurant Achievements
```

---

# Counter Summary

| Item                   | Count |
| ---------------------- | ----: |
| Main Section           |     1 |
| Counter Cards          |     4 |
| CSS Selectors          |     7 |
| JavaScript Functions   |     2 |
| Responsive Breakpoints |     3 |
| Hover Effects          |     1 |

---

========================================================================================================


# 📘 Part 2.4 – Home Page → Categories Section (`index.html`)

---

# 2.4 Categories Overview

| Property            | Details                         |
| ------------------- | ------------------------------- |
| **HTML File**       | `index.html`                    |
| **CSS File**        | `style.css`                     |
| **JavaScript File** | `script.js`                     |
| **Section Type**    | Food Categories                 |
| **Responsive**      | ✅ Desktop • ✅ Tablet • ✅ Mobile |
| **Animation**       | Hover, Reveal                   |

---

# Section Purpose

The **Categories Section** allows users to quickly explore different food categories offered by the restaurant, such as Thalis, Starters, Main Course, Breads, Desserts, and Beverages.

---

# Structure

```text
Home Categories
│
└── home-categories
      │
      ├── section-title
      │
      └── home-category-grid
             │
             ├── home-category-card
             │      ├── category-image
             │      ├── category-name
             │      └── category-btn
             │
             ├── home-category-card
             ├── home-category-card
             └── ...
```

---

# CSS Mapping

| Selector                    | HTML Element | Purpose                  | JS Used | Responsive |
| --------------------------- | ------------ | ------------------------ | :-----: | :--------: |
| `.home-categories`          | `<section>`  | Categories section       |    ❌    |      ✅     |
| `.section-title`            | `<h2>`       | Section heading          |    ❌    |      ✅     |
| `.home-category-grid`       | `<div>`      | Grid layout              |    ❌    |      ✅     |
| `.home-category-card`       | `<div>`      | Individual category card |    ❌    |      ✅     |
| `.category-image`           | `<img>`      | Category image           |    ❌    |      ✅     |
| `.category-name`            | `<h3>`       | Category title           |    ❌    |      ✅     |
| `.category-btn`             | `<a>`        | View category button     |    ✅    |      ✅     |
| `.home-category-card:hover` | CSS          | Hover animation          |    ❌    |      ✅     |

---

# HTML Hierarchy

```text
section.home-categories
│
├── h2.section-title
│
└── div.home-category-grid
      │
      ├── div.home-category-card
      │      ├── img.category-image
      │      ├── h3.category-name
      │      └── a.category-btn
      │
      ├── div.home-category-card
      ├── div.home-category-card
      └── ...
```

---

# JavaScript Interaction

| Function                         | Selector              | Purpose                                |
| -------------------------------- | --------------------- | -------------------------------------- |
| Category Navigation              | `.category-btn`       | Opens Menu page with selected category |
| Scroll Reveal *(if implemented)* | `.home-category-card` | Animates cards into view               |

---

# Responsive Layout

| Device  | Layout            |
| ------- | ----------------- |
| Desktop | 4–6 cards per row |
| Tablet  | 2–3 cards per row |
| Mobile  | 1–2 cards per row |

---

# User Flow

```text
Home Page
     │
     ▼
Categories Section
     │
     ▼
User Selects Category
     │
     ▼
Menu Page Opens
     │
     ▼
Selected Category Displayed
```

---

# Dependency Map

```text
index.html
     │
     ▼
.home-categories
     │
     ├── .section-title
     ├── .home-category-grid
     │
     └── .home-category-card
            ├── .category-image
            ├── .category-name
            └── .category-btn
     │
     ▼
style.css
     │
     ├── Grid Layout
     ├── Card Styling
     ├── Hover Effects
     └── Responsive Rules
     │
     ▼
script.js
     │
     └── Category Navigation
```

---

# Categories Summary

| Item                   |       Count |
| ---------------------- | ----------: |
| Main Section           |           1 |
| Category Cards         | 6 (approx.) |
| CSS Selectors          |           8 |
| JavaScript Functions   |         1–2 |
| Responsive Breakpoints |           3 |
| Hover Effects          |           1 |

---

=======================================================================================================







## 📚 Documentation Roadmap

### 📖 Volume 1 – Introduction

* Cover Page
* Certificate
* Acknowledgement
* Abstract
* Table of Contents
* Project Overview
* Objectives
* Features
* Technology Stack

### 📖 Volume 2 – Project Architecture

* Folder Structure
* MVC Architecture
* Flask Workflow
* Module Diagram
* Request–Response Flow
* System Architecture Diagram

### 📖 Volume 3 – Frontend Documentation

For **every HTML page**:

* Purpose
* UI Sections
* HTML Structure
* CSS Classes Used
* JavaScript Used
* Navigation Flow

Includes:

* `base.html`
* `index.html`
* `menu.html`
* `cart.html`
* `checkout.html`
* `invoice.html`
* `dashboard.html`
* `admin.html`
* `manage_menu.html`
* `manage_reservations.html`
* `login.html`
* `add_dish.html`
* `edit_dish.html`
* and all remaining templates.

### 📖 Volume 4 – CSS Documentation

Every selector:

* Class/ID name
* File location
* HTML page(s)
* Purpose
* Responsive behavior
* Hover/animation
* Related JavaScript

### 📖 Volume 5 – JavaScript Documentation

Every function:

* Function name
* Description
* Parameters
* DOM elements
* Events
* AJAX/Fetch requests
* Flow diagrams

### 📖 Volume 6 – Backend Documentation

For every Python file:

* Purpose
* Routes
* Functions
* Database operations
* Template rendering
* Request flow

### 📖 Volume 7 – Database Documentation

* Database schema
* ER Diagram
* Tables
* Primary Keys
* Foreign Keys
* Relationships

### 📖 Volume 8 – Complete Mapping

* HTML → CSS
* CSS → HTML
* HTML → JS
* JS → HTML
* Flask Route → Template
* Template → Database

### 📖 Volume 9 – Flowcharts

* Customer ordering flow
* Reservation flow
* Admin workflow
* Invoice generation
* QR ordering flow

### 📖 Volume 10 – Reference

* Complete CSS Selector Index
* JavaScript Function Index
* Flask Route Index
* Database Table Index

---

