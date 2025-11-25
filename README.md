# Freight Labs Website

This is the source code for the Freight Labs website, a premium B2B SaaS-style site for a logistics marketing agency.

## Project Structure

- `index.html`: The main homepage with 10 distinct sections.
- `style.css`: Custom CSS with premium gradients, animations, and responsive design.
- `script.js`: Handles scroll animations and mobile navigation.
- `*.png`: Generated assets for the dashboard and mockups.

## Deployment Guide

### Option 1: Netlify Drop (Easiest)

1.  Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2.  Drag and drop the `freightlabs` folder onto the page.
3.  Your site will be live in seconds!

### Option 2: GitHub + Netlify (Recommended for Updates)

1.  **Initialize Git:**
    Open your terminal in the `freightlabs` folder:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

2.  **Push to GitHub:**
    - Create a new repository on GitHub.
    - Run the commands shown by GitHub to push your existing repository:
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/freightlabs.git
    git branch -M main
    git push -u origin main
    ```

3.  **Connect to Netlify:**
    - Log in to Netlify.
    - Click "Add new site" > "Import an existing project".
    - Select GitHub and choose your `freightlabs` repository.
    - Click "Deploy Site".

## Customization

-   **Images:** You can replace the placeholder images in the root directory with your own assets.
-   **Colors:** Edit the `:root` variables in `style.css` to change the color scheme.
-   **Content:** Update the text in `index.html` to match your specific messaging.
