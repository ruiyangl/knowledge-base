# Price Type Options

| **Price Type** | **Description** | **Use Case** | **Risk** |
| --- | --- | --- | --- |
| **Market** | Executes immediately at the best available price. | Quick execution regardless of minor price fluctuations. | Price may differ from expectation during volatile periods. |
| **Market on Close** | Executes as a market order at the **closing price of the trading day**. | Executing orders at the end of the trading session. | Price can fluctuate until the final moments of the session. |
| **Limit** | Executes only at a **specified price or better**. | Precise control over buy/sell price. | Order may not be executed if the market doesn’t reach your price. |
| **Stop on Quote** | Converts to a **market order** when the stock reaches a specified price. | Limiting losses or protecting profits. | Executes as a market order once triggered; price may vary significantly. |
| **Stop Limit on Quote** | Combines a stop order with a limit order. | Ensuring sale or purchase at a specific price or better. | Order may not be filled if the price moves past the limit price. |
| **Trailing Stop $** | Sets a **moving stop order** based on a fixed dollar amount. | Locking in profits as price increases. | Can trigger frequently during volatile periods. |
| **Trailing Stop %** | Similar to **Trailing Stop $**, but based on a **percentage** instead. | Protecting profits using percentage-based movements. | May trigger unexpectedly if sudden price changes occur |