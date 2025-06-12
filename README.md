# Golf Lineup Optimizer

This Python program ranks professional golfers in each tier based on their fit for the Oakmont course, recent performance, and historical Oakmont results. It helps optimize your office pool lineup by selecting the top performers per tier.

---

## Features

* **Course Fit Scoring** (50% weight)

  * **Driving Distance**: Favor long hitters on Oakmont’s lengthy holes
  * **Fairway Accuracy**: Emphasize hitting tight fairways (holes with handicap ≤ 5)
  * **Putting Performance**: Reward players who require fewer putts on Oakmont’s fast greens

* **Recent Form** (30% weight)

  * Simulated via placeholder function; replace with API or web-scraping logic

* **Historical Oakmont Performance** (20% weight)

  * Simulated via placeholder; ideal for integrating 2016 US Open leaderboard data

* **Tiered Player Structure**

  * Six tiers (1–6), each with 10 golfers
  * Computes and prints a sorted ranking of each tier by overall score

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/golf-lineup-optimizer.git
   cd golf-lineup-optimizer
   ```

2. **Install dependencies**

   ```bash
   pip install pandas matplotlib beautifulsoup4 requests
   ```

3. **Place the Oakmont hole data CSV**
   Ensure `Oakmont_Hole_Data__2016_.csv` is in the project root.

---

## Usage

```bash
python golf_lineup_optimizer.py
```

This will load the hole data, simulate player stats, compute scores, and print tier rankings.

---

## Sample Output

```
Tier 1 Rankings (Oakmont fit):
            player  course_score  overall_score
 Xander Schauffele         0.637          0.783
  Scottie Scheffler         0.623          0.698
      Rory McIlroy         0.630          0.641
          Jon Rahm         0.614          0.594
   Tommy Fleetwood         0.626          0.593
Bryson DeChambeau         0.646          0.584
   Joaquin Niemann         0.625          0.558
   Collin Morikawa         0.623          0.505
      Ludvig Aberg         0.632          0.427
       Shane Lowry         0.614          0.388

Tier 2 Rankings (Oakmont fit):
         player  course_score  overall_score
  Tyrrell Hatton         0.638          0.730
   Jordan Spieth         0.615          0.713
   Justin Thomas         0.620          0.694
   Brooks Koepka         0.610          0.678
 Patrick Cantlay         0.610          0.614
   Sepp Straka         0.634          0.586
  Viktor Hovland         0.627          0.574
 Hideki Matsuyama         0.626          0.532
  Russell Henley         0.623          0.488
   Corey Conners         0.605          0.451
```

*(Further tiers omitted for brevity)*

---

## Customization

* **Profile Fetchers**: Replace `fetch_player_profile`, `simulate_recent_performance`, and `simulate_historical_performance` with real data sources (e.g., ESPN API, PGA Tour stats).
* **Weight Adjustments**: Modify `WEIGHT_COURSE`, `WEIGHT_RECENT`, and `WEIGHT_HISTORICAL` to tweak scoring balance.
* **Tier Rosters**: Update the `tier_players` dictionary in `main()` to reflect custom pools.

---

## License

Shamil Tajuddin
