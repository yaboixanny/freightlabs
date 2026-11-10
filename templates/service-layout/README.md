# Freight Labs service-page layout

Approved source: `seo-trucking-companies/index.html`, saved November 10, 2026.
`reference.html.template` is the complete approved source snapshot, retained for layout fidelity. It is a reference file, not a published URL.

## Reuse

Use `assets/service-layout.css` and the `service-layout-page` body class. The shared components use the `service-layout-` prefix. `pages.json` records the 17 adapted service pages, their card content, service categories, and hero assets. The trucking SEO page remains the original approved implementation.

Keep this page order:

1. Existing service-specific hero headline and lead, rounded CTA, channel badges, square WebP photo with rounded corners and a factual text overlay.
2. Service problem and process sections.
3. Nine service cards in three desktop columns; two supporting panels appropriate to the service.
4. Service strategy, when present.
5. Timeline with four steps and three compact visuals.
6. Quick explanation with a checklist and paired facts panel.
7. Rounded orange “Book a call with Alex” banner.
8. Relevant existing proof, reporting, or portfolio sections.
9. Existing service pricing and plan details.
10. Light FAQ section with numbered, rounded question bubbles and a “Your [Service] Questions, Answered” heading.
11. Closing CTA and the site's existing footer.

## Content and links

Keep URLs, canonical tags, titles, main headings, service details, prices, plan limits, FAQ answers, and existing useful links specific to the page. Write new copy in short, plain sentences. Do not add unsupported client counts, results, or experience claims.

SEO pages use SEO/GEO panels and may link contextually to `/ai-seo-logistics/`. AI search must not link to itself. Paid media uses campaign/lead tracking panels; outbound uses account research/outreach; websites use buyer experience/build delivery; content uses planning/publishing; consulting uses planning/action. Do not copy trucking terms or SEO promises onto unrelated services.

Use existing licensed site images or verified free stock images. Store shared optimized WebP assets under `assets/service-heroes/`, with explicit image dimensions, descriptive alt text, and high fetch priority for the hero. Avoid image-generation dashboards in place of a relevant hero photo.

## Checks before publishing

- Verify one main heading, nine service cards, two supporting panels, one hero photo, one FAQ block, and unique IDs.
- Keep hero headings, canonical URLs, and pricing consistent with the page's approved source.
- Verify image, stylesheet, internal link, and fragment destinations.
- Match visible FAQs to FAQ structured data when editing questions or answers.
- Check three-column desktop and single-column mobile layouts, readable colors, image loading, and accordion behavior.
- Run `git diff --check` and `python3 tools/update-csp-hashes.py --check`.

The removed free-audit banner and one-year roadmap are not part of the approved layout.
