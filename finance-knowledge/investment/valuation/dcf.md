# DCF

This page will demonstrate how to best calculate the DCF for a given stock

1. Explicit forecast period
2. terminal value
3. Market 

## step 1

Free Cash Flow (FCF) = Operating Cash Flow - Capital Expenditures

<details markdown="1">
<summary> How do we get to FCF</summary>

Sales  
Operating profit = Sales x Operating profit margin  
Cash taxes = Operating profit x Cash tax rate  
NOPAT = Operating profit - Cash tax  
Total investment = Incremental fixed-capital investment + Incremental working-capital investment   
FCF = NOPAT - Total Investment

* Operating income ≈ operating profit ≈ EBIT
* Sales ≈ revenue ≈ the Top Line

</details>

## step 2

choose Explicit Forecast Period

The forecast period is the time that the market
expects a company to generate returns on incremental investment
that exceed its cost of capital. Do not pick an arbitrary period

~ 5yr

Forecast FCF Growth 

| year | Growth Assumption | Explanation | FCF calc | FCF |
| --- | --- | --- | --- | --- |
| 0 | -5% | Ressession  | Given | 1.58 |
| 1 | -27% | Stablization | Prediction (-27%) | 1.16 |
| 2 | +8% | Early Recovery | prediction (+8%) | 1.25 |
| 3 | +8% | Normalization | +8% | 1.35 |
| 4 | +8% | Mature growth | +8% | 1.5 |
| 5 | +8% |  |  | 1.57 |

## Step 4

Choose a Discount Rate (WACC)

~9.5%

<details markdown="1">
<summary> WACC calculation </summary>

given a company plans on raise capital in the proportion of 20 percent debt and 80 percent equity

|| Weight | cost | weighted cost|
| --- | --- | --- | --- |
| Debt (after tax) | 20 | 4.0 | 0.8 |
| Equity | 80 | 9.0 | 7.2 |
| Cost of capital | | | 8.0|

- After-tax cost of debt-financed instruments = Yield-to-maturity on long-term debt × (1 − Tax rate)
- Cost of equity = Risk-free rate + Equity risk premium
- Equity risk premium = Beta × Market risk premium
- Market risk premium = Expected market rate of return − Risk-free rate

Cost of equity = Risk-free rate + Beta × (Expected market rate of return − Risk-free rate)
</details>

## step 5

Present Value = 

$$
Present Value = \frac{FCF}{(1+r)^t}
$$

| year | FCF | WACC | PV |
| --- | --- | --- | --- |
| 1 | 1.16 | 1/1.095^1 | 1.059 |
| 2 | 1.25 | 1/1.095^2 | 1.043 |
| 3 | 1.35 | 1/1.095^3 | 1.028 |
| 4 | 1.5 | 1/1.095^4 | 1.043 |
| 5 | 1.57 | 1/1.095^5 | 1 |

Sum = 5.175

## step 6

Calculate terminal value (continuing value)

<details markdown="1">
<summary> Continuing value estimate </summary>

The key is to consider carefully what the company’s competitive position will be at the end of the explicit forecast period.


- Inputs
  - Cost of capital 
    - after the explicit forecasting period
    - cost of capital often declines as companies mature
  - Inflation
    - If a company has pricing prower. prefer low price elasticity
  - growth betyond explicit forecasting period
    - long-term moat

</details>


There are four recomanded way of calculating terminal value (Expectations investing, Mauboussin et. al.)
- perpetuity
- perpetuity-with-inflation
- perpetuitywith-partial-inflation
- perpetuity-with-decline.

### Perpetuity Method

company generating returns greater than its cost of capital will attract competition that will drive returns on new investments down to the cost of capital by the end of the forecast period. Hense company will continuously generate no more than the cost of capital.

$$
Present\ value\ of\ a\ perpetuity\ =\ \frac{NOPAT_{at\ the\ end\ of\ the\ forecast\ period}}{Cost\ of\ Capital}
$$

Don't worry too much about why NOPAT is used this has to do with investment beyond forcast period generates no furtuer return.

The perpetuity method assumes that while a business earns the
cost of capital in the post-forecast period, its cash flow growth
does not keep up with the rate of inflation.

### Perpetuity-with-inflation method

cash flows will grow annually at the inflation rate in the post-forecast period

$$
perpetuity\ with\ inflation = \frac{NOPAT_{at\ the\ end\ of\ the\ forecast\ period} × (1 + Inflation\ rate)}{Cost\ of\ capital\ -\ Inflation\ rate}
$$

In the rare case that you expect a company to not only match the rate of inflation but also grow above and beyond it, you can substitute a growth term for inflation

### Perpetuity-with-partial-inflation method

the perpetuity will grow annually in the post-forecast period at the rate greater than zero but less than the full inflation rate.

$$
perpetuity\ with\ inflation = \frac{NOPAT_{at\ the\ end\ of\ the\ forecast\ period} × [1 + (p\ ×\ Inflation\ rate)]}{Cost\ of\ capital\ -\ (p\ ×\ Inflation\ rate)}
$$

Most appropriate for most companies and should be used as defualt

### Perpetuity-wit-Decline Method

$$
perpetuity\ with\ inflation = \frac{NOPAT_{at\ the\ end\ of\ the\ forecast\ period} × (1 - Decline)}{Cost\ of\ capital\ +\ Decline}
$$



> **Notice:**
> enterprise discounted cash flow is approapreate for nonfinancial companies while equity discounted cashf low is for financial services




$$
TV = \frac{FCF_{year6}}{r-g} = 22.4B
$$

discount this to today → 22.4 / 1.095^5 = 14.2472490642

## Step 7

add them together = corperate value = 19.4222490642

FCF = EBITA - tax + non-cash expenditure - Capex - working capital investment

So we know, the DFC depends on r, which is also WACC ( Weighted Average Cost of Capital )

This mostly differ by industry, here is an [example](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html?utm_source=chatgpt.com)

A higher WACC usually indicate that an industry is more risky and prune to credit risk. Normally, WACC = riskfree rate + risk preminum for the industry

This mean that fed rate cut will decrease descounted rate.  which increase equity price

Big tech stocks are highly sensitve because their value relies on future earnings. any change in the future discount rate will affect them significantly


corporate value = present value of free cash flows for the forecasting period + continuing value

Shareholder value = corporate value + nonoperating assets minus debt



# Reverse DCF

Calculated using MU Q4,2026 result as an example

## Step 1

gather:

- **Operating value: $1,017.** Of the $1,065 price, $48 is net cash; the remaining $1,017 is what you pay for the business itself.
- **Required return* (r): 10–14%,** with 3% perpetual growth (**g**) after the forecast period. As discussed, 10–11% is closer to what practitioners use.
- **Cash conversion: ~0.70.** Micron reinvests heavily in fabs, so only about 70 cents of each EPS dollar is cash an owner could take out. FY26 was 72%.

*Here Claude used cost of equity, strictly this is different from WACC. 

| If you discount… | Use… | You get… |
| --- | --- | --- |
| Cash flow to the whole company, before interest | WACC (the blended cost of debt and equity) | Enterprise value, then subtract net debt to get the equity |
| Cash flow to shareholders, after interest | Cost of equity | Equity value per share directly |

EPS is earnings after interest, so that’s cash flow to shareholders, and the right rate is the cost of equity. When the debt of a company is low relative to it’s equity value, the difference is negligible.

The way to understand r is: During DCF calculation, we discount the future return because there is a monitory opportunity cost to that return, so we need to discount that from the future return. During rDCF, we are requiring a certain return to justify the spending of the capital. 

## Step 2

Calculate Implied permanent EPS

$$
Permanent\ Cash\ Flow = operating\ value × (r − g).
$$

$$
EPS_{nonGAPP} = \frac{Cash\ flow}{FCF\ Conversion\ Rate}
$$

permanent cash flow = $1017 * (0.12 - 0.3) = $91.50

EPS = $91.50 / 0.7 = $128

this is asking a $128 EPS per year perpetually .

### Step 3

Calculate implied growth