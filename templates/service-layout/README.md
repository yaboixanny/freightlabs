# Freight Labs service-page layout

Core references: `seo-trucking-companies/index.html` and `freightseo/index.html`. The approved snapshots are saved as `reference.html.template` and `logistics-reference.html.template`; these are reference files, not published URLs.

## Reuse

Use `assets/service-layout.css` and the `service-layout-page` body class. The shared components use the `service-layout-` prefix. `pages.json` records the 17 adapted service pages, their card content, service categories, and hero assets. The trucking SEO page remains the original approved implementation.

Keep this page order:

1. Existing service-specific hero headline and lead, rounded CTA, channel badges, square WebP photo with rounded corners and a factual text overlay.
2. Service problem and process sections.
3. Nine service cards in three desktop columns; two supporting panels appropriate to the service.
4. Service strategy, when present.
5. Timeline with four steps and three illustrated browser-style panels, using service-appropriate timing and copy.
6. Quick explanation with a detailed checklist and facts panel; vertically center the left content alongside the right panel on desktop.
7. Rounded orange “Book a call with Alex” banner.
8. Pricing follows the same custom-plan widget as the two core pages.
9. Light FAQ section with numbered, rounded question bubbles and a “Your [Service] Questions, Answered” heading.
10. Closing CTA and the site's existing footer.

Do not add standalone sections that are absent from both core references.

## Content and links

Keep URLs, canonical tags, titles, main headings, service details, FAQ answers, and relevant existing links specific to the page. Hero subtitles should explain the current service without links or appended cross-promotions. Platform badges use the approved 10% larger text and icons, with tighter padding at narrow laptop widths to keep one row. Write new copy in short, plain sentences. Do not add unsupported client counts, results, or experience claims.

SEO pages use SEO/GEO panels and may link contextually to `/ai-seo-logistics/`. AI search must not link to itself. Paid media uses campaign/lead tracking panels; outbound uses account research/outreach; websites use buyer experience/build delivery; content uses planning/publishing; consulting uses planning/action. Do not copy trucking terms or SEO promises onto unrelated services.

Use existing licensed site images or verified free stock images. Store shared optimized WebP assets under `assets/service-heroes/`, with explicit image dimensions, descriptive alt text, and high fetch priority for the hero. Avoid image-generation dashboards in place of a relevant hero photo.

## Checks before publishing

- Verify one main heading, nine service cards, two supporting panels, one hero photo, one FAQ block, and unique IDs.
- Keep hero headings and canonical URLs consistent with the page's approved source; use the shared custom pricing widget.
- Verify image, stylesheet, internal link, and fragment destinations.
- Match visible FAQs to FAQ structured data when editing questions or answers.
- Check three-column desktop and single-column mobile layouts, readable colors, image loading, and accordion behavior.
- Run `git diff --check` and `python3 tools/update-csp-hashes.py --check`.

The removed free-audit banner and one-year roadmap are not part of the approved layout.
