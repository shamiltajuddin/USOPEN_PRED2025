import pandas as pd
import random
from typing import List, Dict

# ========== CONFIGURATION ===========
random.seed(42)  # For reproducible results in placeholders

# Updated Weight settings
WEIGHT_COURSE = 0.5       # increased importance of course fit
WEIGHT_RECENT = 0.3       # moderate importance of recent form
WEIGHT_HISTORICAL = 0.2   # historical Oakmont performance

# ========== DATA LOADERS ===========

def load_hole_data(csv_path: str) -> pd.DataFrame:
    """
    Load course hole data (distance, average score, handicap).
    """
    df = pd.read_csv(csv_path)
    # Normalize hole metrics for scoring
    df['distance_norm'] = df['Hole Distance (Yards)'] / df['Hole Distance (Yards)'].max()
    df['difficulty_norm'] = (
        df['Average Score (2016)'] - df['Average Score (2016)'].min()
    ) / (
        df['Average Score (2016)'].max() - df['Average Score (2016)'].min()
    )
    return df

# ========== DATA FETCHERS (PLACEHOLDERS) ===========

def fetch_player_profile(player_name: str) -> Dict[str, float]:
    """
    Placeholder for fetching real player stats.
    Returns:
        - driving_distance (yards)
        - fairway_accuracy (0-1)
        - putting_avg (putts per hole)
    """
    return {
        'driving_distance': random.uniform(280, 320),  # avg driving distance
        'fairway_accuracy': random.uniform(0.55, 0.75),
        'putting_avg': random.uniform(1.70, 1.85)
    }

# ========== SCORING FUNCTIONS ===========

def score_course_fit(player_stats: Dict[str, float], hole_data: pd.DataFrame) -> float:
    """
    Calculate course_score by combining:
      1. drive_score  = normalized driving_distance × mean normalized hole length
      2. accuracy_score = fairway_accuracy × fraction of narrow holes (handicap ≤ 5)
      3. putting_score = baseline_putts (2.0) ÷ player's putts per hole
    """
    drive_score = (player_stats['driving_distance'] / 350) * hole_data['distance_norm'].mean()
    narrow_fraction = (hole_data['Handicap (2016)'] <= 5).sum() / len(hole_data)
    accuracy_score = player_stats['fairway_accuracy'] * narrow_fraction
    putting_score = 2.0 / player_stats['putting_avg']
    # Average components for final course fit
    return (drive_score + accuracy_score + putting_score) / 3


def simulate_recent_performance(player_name: str) -> float:
    """
    Placeholder: generates a pseudo-random 0–1 recent form score.
    """
    return (hash(player_name[::-1]) % 50 + random.random()) / 50


def simulate_historical_performance(player_name: str) -> float:
    """
    Placeholder: generates a pseudo-random 0–1 historical Oakmont score.
    """
    return (hash(player_name.upper()) % 50 + random.random()) / 50


def compute_overall_scores(players: List[str], hole_data: pd.DataFrame, tier: int) -> pd.DataFrame:
    """
    Compute weighted overall_score for each player:
      overall_score = (0.5 × course_score) + (0.3 × recent_score) + (0.2 × historical_score)
    """
    rows = []
    for player in players:
        stats = fetch_player_profile(player)
        course_score = score_course_fit(stats, hole_data)
        recent_score = simulate_recent_performance(player)
        hist_score = simulate_historical_performance(player)
        overall = (
            WEIGHT_COURSE * course_score +
            WEIGHT_RECENT * recent_score +
            WEIGHT_HISTORICAL * hist_score
        )
        rows.append({
            'player': player,
            'tier': tier,
            'course_score': round(course_score, 3),
            'recent_score': round(recent_score, 3),
            'historical_score': round(hist_score, 3),
            'overall_score': round(overall, 3)
        })
    df = pd.DataFrame(rows)
    return df.sort_values('overall_score', ascending=False)

# ========== RANKING & OUTPUT ===========

def main():
    hole_data = load_hole_data('Oakmont_Hole_Data__2016_.csv')
    tier_players = {
        1: ['Scottie Scheffler', 'Bryson DeChambeau', 'Rory McIlroy', 'Jon Rahm',
            'Xander Schauffele', 'Collin Morikawa', 'Ludvig Aberg', 'Joaquin Niemann',
            'Tommy Fleetwood', 'Shane Lowry'],
        2: ['Justin Thomas', 'Patrick Cantlay', 'Sepp Straka', 'Tyrrell Hatton',
            'Brooks Koepka', 'Viktor Hovland', 'Jordan Spieth', 'Russell Henley',
            'Corey Conners', 'Hideki Matsuyama'],
        3: ['Ben Griffin', 'Sam Burns', 'Keegan Bradley', 'Harris English', 'Tony Finau',
            'Maverick McNealy', 'Robert MacIntyre', 'Ryan Fox', 'Si Woo Kim', 'Daniel Berger'],
        4: ['Taylor Pendrith', 'Matthew Fitzpatrick', 'Patrick Reed', 'Sungjae Im',
            'Justin Rose', 'Jason Day', 'Aaron Rai', 'Cameron Young', 'J.J. Spaun', 'Akshay Bhatia'],
        5: ['Min Woo Lee', 'Wyndham Clark', 'Cameron Smith', 'Denny McCarthy', 'Adam Scott',
            'J.T. Poston', 'Nick Taylor', 'Dustin Johnson', 'Andrew Novak', 'Thorbjørn Olesen'],
        6: ['Brian Harman', 'Jinichiro Kozuma', 'Michael Kim', 'Davis Thompson', 'Joohyung Kim',
            'Carlos Ortiz', 'Gary Woodland', 'Marc Leishman', 'Byeong Hun An', 'Max Greyserman']
    }
    for tier, players in tier_players.items():
        df_ranked = compute_overall_scores(players, hole_data, tier)
        print(f"\nTier {tier} Rankings (Oakmont fit):")
        print(df_ranked[['player', 'course_score', 'overall_score']].to_string(index=False))

if __name__ == '__main__':
    main()
