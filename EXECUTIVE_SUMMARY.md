# Executive Summary — Sales Performance Analysis

**Period covered:** July 2024 – June 2026 · **Orders analyzed:** 8,000 · **Total net revenue:** $1,802,685

## Key Findings

**Regional performance is uneven.** East leads with $418,017 in net revenue, roughly 49% ahead of the lowest-performing region, Central ($280,247). Ravi Shah (East) is the top individual rep at $147,741. Central also has the highest return rate of any region (6.74%), suggesting its revenue gap may be compounded by a fulfillment or product-fit issue worth investigating alongside the pure sales shortfall.

**Revenue is seasonal, and the holiday spike is partly a discounting effect.** December is the strongest month for net revenue ($111,117), but it also carries the deepest average discounting of the year ($22,965 in discounts given, roughly 17% of gross). January is the weakest month ($49,065 net), consistent with a typical post-holiday pullback. The takeaway: December's revenue peak is real, but a meaningful share of it is being bought with margin.

**Discounting is fairly even across categories, with no clear outlier.** Effective discount rates range narrowly from 9.4% (Office Supplies) to 9.7% (Electronics) — a roughly half-point spread. This suggests discount policy is being applied consistently across the catalog rather than concentrated in one category, so there's no single product line driving margin erosion.

**Wholesale is the least efficient channel.** Wholesale generates the least revenue ($138,249, only 8% of total) yet carries by far the highest average discount (19.9%, roughly double every other channel) and the highest return rate (6.67%). Online is the clear engine of the business: 44% of net revenue ($785,188) at a modest 7.4% average discount and the lowest return rate among channels tied with In-Store.

**Returns are elevated but not alarming, and cluster around Wholesale.** Overall return rate is 5.53%. No single category stands out (all fall in a tight 5.3%–5.9% band), but Wholesale orders return at 6.67% — the highest of any channel — reinforcing the case that Wholesale deserves a closer look on both margin and quality grounds.

## Recommendations

1. Investigate Central region's combination of lower revenue and higher returns — this looks like more than a sales-volume problem.
2. Review whether Wholesale's deep discounting is earning proportionate revenue; consider tightening discount tiers or renegotiating minimum order economics.
3. Treat December's revenue as partly discount-subsidized when setting next year's holiday promotion budget and margin targets.

## Methodology

Analysis based on a synthetic sales transactions dataset (`data/synthetic_sales_data.csv`, 8,000 rows) covering 5 regions, 5 product categories, 25 products, and 4 sales channels. Five SQL queries (`sql/queries.sql`) were run and validated against source totals (see `run_queries.py`); results are in `results/`, charts in `charts/`, and an interactive dashboard in `dashboard/dashboard.html`.

*Note: this dataset is synthetic and generated for demonstration purposes — figures do not represent real sales.*
