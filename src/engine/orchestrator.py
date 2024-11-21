from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from catboost import CatBoostClassifier

import pandas as pd

dataset = 'E:\Projetos\Personal\TCC\dataset_full-modified.csv'
data = pd.read_csv(dataset)

features = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url', 'qty_tilde_url', 'qty_comma_url', 'qty_plus_url', 'qty_asterisk_url', 'qty_hashtag_url', 'qty_dollar_url', 'qty_percent_url', 'qty_tld_url', 'length_url', 'qty_dot_domain', 'qty_hyphen_domain', 'qty_underline_domain', 'qty_slash_domain', 'qty_questionmark_domain', 'qty_equal_domain', 'qty_at_domain', 'qty_and_domain', 'qty_exclamation_domain', 'qty_space_domain', 'qty_tilde_domain', 'qty_comma_domain', 'qty_plus_domain', 'qty_asterisk_domain', 'qty_hashtag_domain', 'qty_dollar_domain', 'qty_percent_domain', 'qty_vowels_domain', 'domain_length', 'domain_in_ip', 'server_client_domain']

x = data[features]
y = data["phishing"]

def run_decision_tree(sample):
  model = DecisionTreeClassifier()

  model.fit(x, y)

  prediction = model.predict(sample)
  confidence = model.predict_proba(sample)
  return prediction[0], confidence[0][prediction[0]]

def run_xg_boost(sample):
  model = XGBClassifier(eval_metric='logloss')

  model.fit(x, y)

  prediction = model.predict(sample)
  confidence = model.predict_proba(sample)
  return prediction[0], confidence[0][prediction[0]]

def run_random_forest(sample):
  model = RandomForestClassifier()

  model.fit(x, y)

  prediction = model.predict(sample)
  confidence = model.predict_proba(sample)
  return prediction[0], confidence[0][prediction[0]]

def run_extra_trees(sample):
  model = ExtraTreesClassifier()

  model.fit(x, y)

  prediction = model.predict(sample)
  confidence = model.predict_proba(sample)
  return prediction[0], confidence[0][prediction[0]]

def run_cat_boost(sample):
  model = CatBoostClassifier(iterations=1000, learning_rate=0.1, depth=6, silent=True)

  model.fit(x, y)

  prediction = model.predict(sample)
  confidence = model.predict_proba(sample)
  return prediction[0], confidence[0][prediction[0]]

def run_logical_regression(sample):
  model = LogisticRegression(max_iter=700)

  model.fit(x, y)

  prediction = model.predict(sample)
  confidence = model.predict_proba(sample)

  return prediction[0], confidence[0][prediction[0]]

def orchestrate(sample):
  sample = pd.DataFrame(sample, columns=features)

  dt_prediction, dt_confidence = run_decision_tree(sample)
  
  if dt_confidence < 0.9 or dt_confidence > 0.985:
    xg_prediction, xg_confidence = run_xg_boost(sample)
    if xg_confidence < 0.9 or xg_confidence > 0.985:
      lr_prediction, lr_confidence = run_logical_regression(sample)
      if lr_prediction < 0.9 or lr_prediction > 0.985:
        rf_prediction, rf_confidence = run_random_forest(sample)
        if rf_confidence < 0.9 or rf_confidence > 0.985:
          et_prediction, et_confidence = run_extra_trees(sample)
          if et_confidence < 0.9 or et_confidence > 0.985:
            cb_prediction, cb_confidence = run_cat_boost(sample)
            return cb_prediction, cb_confidence
          else:
            return et_prediction, et_confidence
        else:
          return rf_prediction, rf_confidence
      else:
        return dt_prediction, dt_confidence
    else:
      return xg_prediction, xg_confidence
  else: 
    return lr_prediction, lr_confidence