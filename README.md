# Content Recommendation API

The content recommendation api is used to provide recommendations for related content based on the underlying
content graph stored as a Neo4j Database. The API can also be used to provide explainable content recommendations
where relations to related content are explained.

The API is used to power chatbots, voice apps (Google Assistant / Alexa), and web applications for media sites.
It provides endpoints for things like summaries, related content, and explainable related content.
The API is responsible for interacting with the neo4j database which hosts the content graph.


## Endpoints

### POST /explore
Takes a url of an article in the graph and finds the corresponding title.
- Finds the most similar articles to that title
- Explains connections from original article to related articles in terms of concepts, entities, and topics.

**Request Params**
- article_url (Must be article in the graph)

Returns a JSON response with the processed original article as well as data on the related articles.

**Sample Request**
```json
{
    "article_url": "https://www.health.harvard.edu/blog/the-health-effects-of-marijuana-from-recreational-and-medical-use-2016081910180",
    "user_id": 1,
    "processor_id": "language-processor-health"
}
```

**Sample Response**
```json
{
    "initial": [
        {
            "title": "Medical marijuana - Harvard Health Blog",
            "date": "2018-01-15 15:30:09+00:00",
            "url": "https://www.health.harvard.edu/blog/the-health-effects-of-marijuana-from-recreational-and-medical-use-2016081910180",
            "summary": "There are few subjects that can stir up stronger emotions among doctors, scientists, researchers, policy makers, and the public than medical marijuana. Is it safe? Is medical marijuana just a ploy to legalize marijuana in general? The Obama administration did not make prosecuting medical marijuana even a minor priority. About 85% of Americans support legalizing medical marijuana, and it is estimated that at least several million Americans currently use it. Marijuana itself has more than 100 active components. In particular, marijuana appears to ease the pain of multiple sclerosis, and nerve pain in general. Other patients are already using medical marijuana, but dont know how to tell their doctors about this for fear of being chided or criticized. My advice for doctors is that whether you are pro, neutral, or against medical marijuana, patients are embracing it, and although we dont have rigorous studies and gold standard proof of the benefits and risks of medical marijuana, we need to learn about it, be open-minded, and above all, be non-judgmental."
        }
    ],
    "related": [
        {
            "title": "Acupuncture for headache - Harvard Health Blog",
            "summary": "It is easy to ridicule a 2000-year-old treatment that can seem closer to magic than to science. Indeed, from the 1970s to around 2005, the skeptics point of view was understandable, because the scientific evidence to show that acupuncture worked, and why, was weak, and clinical trials were small and of poor quality. How do we know if acupuncture really works for pain? Is acupuncture really that good? Indeed, the question of whether acupuncture points actually exist has been largely avoided by the acupuncture research community, even though acupuncture point terminology continues to be used in research studies. Acupuncture for Patients With Migraine: A Randomized Controlled Trial. Acupuncture in Medicine, December 2001. Acupuncture in Medicine, June 2014.",
            "url": "https://www.health.harvard.edu/blog/acupuncture-for-headache-2018012513146",
            "img_url": "https://hhp-blog.s3.amazonaws.com/2018/01/iStock-139869255-1024x683.jpg",
            "date": "2018-01-25 15:30:11+00:00",
            "entities": [],
            "concepts": [],
            "entity_categories": [
                {
                    "entity": "Migraine",
                    "relation": "DiseaseOrMedicalCondition"
                },
                {
                    "entity": "headache",
                    "relation": "Disease"
                },
                {
                    "entity": "JAMA",
                    "relation": "City"
                },
                {
                    "entity": "headache",
                    "relation": "DiseaseOrMedicalCondition"
                },
                {
                    "entity": "Migraine",
                    "relation": "RiskFactor"
                }
            ]
        },
        {
            "title": "Managing pain after surgery - Harvard Health Blog",
            "summary": "Surgery and pain pills used to go hand in hand. After all, you need a strong prescription pain medication to ensure you arent in pain after a procedure, right? Turns out not only is prescription pain medication not always needed, but often not advisable after surgery, because it can raise the risk of opioid addiction. As a result, surgeons today are rethinking post-surgical pain management strategies. Today, surgeons like her are increasingly turning toward non-opioid medications and other options to manage pain. In many cases, non-opioid pain relievers, such as ibuprofen (Advil) and acetaminophen (Tylenol), will control postsurgical pain if taken as recommended. Limit opioid medication use. When people are having surgery, they should expect to have some pain or discomfort, says Dr. Matzkin. While no one should have to endure excruciating pain, having some pain is okay. Letting people know that its okay to have some pain can actually reduce the amount of pain medications required, says Dr. Chiodo. Use nonmedication strategies to manage pain.",
            "url": "https://www.health.harvard.edu/blog/managing-pain-after-surgery-2019020715940",
            "img_url": "https://hhp-blog.s3.amazonaws.com/2019/02/iStock-641571590-1024x681.jpg",
            "date": "2019-02-07 15:30:07+00:00",
            "entities": [
                {
                    "label": "United States"
                },
                {
                    "label": "Advil"
                }
            ],
            "concepts": [
                {
                    "label": "Pain"
                }
            ],
            "entity_categories": [
                {
                    "entity": "United States",
                    "relation": "AdministrativeDivision"
                },
                {
                    "entity": "United States",
                    "relation": "GovernmentalJurisdiction"
                }
            ]
        },
        {
            "title": "Cannabidiol (CBD) — what we know and what we don’t - Harvard Health Blog",
            "summary": "Cannabidiol (CBD) has been recently covered in the media, and you may have even seen it as an add-in booster to your post-workout smoothie or morning coffee. What exactly is CBD? CBD stands for cannabidiol. While CBD is a component of marijuana (one of hundreds), by itself it does not cause a high. To date, there is no evidence of public health related problems associated with the use of pure CBD. Currently, many people obtain CBD online without a medical cannabis license. The governments position on CBD is confusing, and depends in part on whether the CBD comes from hemp or marijuana. In numerous studies, CBD was able to reduce the number of seizures, and in some cases it was able to stop them altogether. CBD may offer an option for treating different types of chronic pain. More study in humans is needed in this area to substantiate the claims of CBD proponents about pain control. Side effects of CBD include nausea, fatigue and irritability.",
            "url": "https://www.health.harvard.edu/blog/cannabidiol-cbd-what-we-know-and-what-we-dont-2018082414476",
            "img_url": "https://hhp-blog.s3.amazonaws.com/2018/08/iStock-1015545230-1024x683.jpg",
            "date": "2018-08-24 10:30:52+00:00",
            "entities": [
                {
                    "label": "marijuana"
                },
                {
                    "label": "United States"
                },
                {
                    "label": "insomnia"
                },
                {
                    "label": "nausea"
                }
            ],
            "concepts": [
                {
                    "label": "Cannabis"
                },
                {
                    "label": "Pain"
                },
                {
                    "label": "Tetrahydrocannabinol"
                }
            ],
            "entity_categories": [
                {
                    "entity": "nausea",
                    "relation": "Symptom"
                },
                {
                    "entity": "epilepsy",
                    "relation": "DiseaseOrMedicalCondition"
                },
                {
                    "entity": "insomnia",
                    "relation": "DiseaseOrMedicalCondition"
                },
                {
                    "entity": "insomnia",
                    "relation": "Symptom"
                },
                {
                    "entity": "Lennox-Gastaut syndrome",
                    "relation": "DiseaseOrMedicalCondition"
                }
            ]
        }
    ]
}
```


### POST /summary
Route takes the url of an article
- Downloads article
- Processed article using the language-processor api

**Request Params**
- article_url (Not required to be in graph)
- processor_id (The id of the cloud function used to process the text, different cloud functions for different Gensim Doc2Vec models. Ie: Health, Tech ...)

Returns JSON containing the summary.


**Sample Request**
```json
{
    "article_url": "https://www.health.harvard.edu/blog/conflict-of-interest-in-medicine-2018100114940",
    "user_id": 1,
    "processor_id": "language-processor-health"
}
```

**Sample Response**
```json
{
    "initial": [
        {
            "title": "Conflict of interest in medicine - Harvard Health Blog",
            "date": "2018-10-01 14:30:00+00:00",
            "url": "https://www.health.harvard.edu/blog/conflict-of-interest-in-medicine-2018100114940",
            "summary": "Recent news reports described an ethical lapse by a prominent New York City cancer specialist. In research published in prominent medical journals, he failed to disclose millions of dollars in payments he had received from drug and healthcare companies that were related to his research. The thinking is that other researchers, doctors, patients, regulators, investors  everyone! But do their patients want to know? Would it matter to you if your doctor accepted gifts, meals, or cash payments from drug companies? Should he or she meet with representatives from pharmaceutical companies who are promoting their latest drugs? Should your doctor attend medical meetings where drug companies sponsor the speaker (complete with dinner in a fancy restaurant)? Is it reasonable for doctors to receive payments to enroll patients in a study sponsored by a drug company? And these are just a few of the many ethical dilemmas that many doctors face."
        }
    ],
    "related": []
}
```


### POST /summary-related:
Route takes the url of an article
- Downloads article
- Finds most similar articles by embedding

**Request Params**
- article_url (Not required to be in graph)
- processor_id

Return JSON containing data on processed original article as well as top 3 related articles.

**Sample Request**
```json
{
    "article_url": "http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html",
    "user_id": 1,
    "processor_id": "language-processor-health"
}
```

**Sample Response**
```json
{
    "initial": [
        {
            "title": "Study: Hospital-Physician Vertical Integration Has Little Impact on Quality of Care; Greater Market Concentration Reduces It",
            "date": "None",
            "url": "http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html",
            "summary": "According to a recent Modern Healthcare CEO Power Panel survey, there is less of an appetite for mergers and acquisitions this year than in 2018. In 2019, 12.5% of CEOs said M&A best describes their growth strategy, down from 25.8% in 2018. Among the 29 data points studied, the researchers analyzed hospital readmission rates, process of care measurements that gauge how well a hospital provides care to its patients, and patient satisfaction scores. Using that information, they tested whether patient outcomes are influenced by greater hospital market concentration or vertical integration between hospitals and physicians. Before they launched their study, the researchers hypothesized that decreased fragmentation, meaning better coordination among a patient's primary care physician, specialists and admitting and attending hospital physicians, could improve patient care. \"Therefore, we need further research on the ability of patient satisfaction to reflect clinical quality, and if it does not, we need to develop and provide to patients better measures in terms that patients can understand and use.\""
        }
    ],
    "related": [
        {
            "title": "Conflict of interest in medicine - Harvard Health Blog",
            "summary": "Recent news reports described an ethical lapse by a prominent New York City cancer specialist. In research published in prominent medical journals, he failed to disclose millions of dollars in payments he had received from drug and healthcare companies that were related to his research. The thinking is that other researchers, doctors, patients, regulators, investors  everyone! But do their patients want to know? Would it matter to you if your doctor accepted gifts, meals, or cash payments from drug companies? Should he or she meet with representatives from pharmaceutical companies who are promoting their latest drugs? Should your doctor attend medical meetings where drug companies sponsor the speaker (complete with dinner in a fancy restaurant)? Is it reasonable for doctors to receive payments to enroll patients in a study sponsored by a drug company? And these are just a few of the many ethical dilemmas that many doctors face.",
            "url": "https://www.health.harvard.edu/blog/conflict-of-interest-in-medicine-2018100114940",
            "img_url": "https://hhp-blog.s3.amazonaws.com/2018/09/iStock-885099664-1024x683.jpg",
            "date": "2018-10-01 14:30:00+00:00",
            "entities": [
                {
                    "label": "researcher"
                },
                {
                    "label": "New York City"
                },
                {
                    "label": "rheumatoid arthritis"
                }
            ],
            "concepts": [
                {
                    "label": "Pharmacology"
                },
                {
                    "label": "Clinical trial"
                },
                {
                    "label": "Pharmaceutical industry"
                }
            ]
        },
        {
            "title": "Physician burnout can affect your health - Harvard Health Blog",
            "summary": "There is a severe and worsening epidemic of physician burnout in the United States, which threatens the health of doctors and patients alike. What is burnout? How does it affect doctors? And, how can this affect patient care? What does physician burnout look like? Annually, approximately 400 physicians take their own lives in the United States. A 2016 study published by the Mayo Clinic showed a high and increasing rate of physician burnout. In other words, more than half of US physicians are experiencing at least some degree of burnout. Moreover, many doctors are leaving medicine mid-career, which, among other things, causes patients to have to start all over again with a new doctor. Other physicians are cutting back their hours, which makes it more difficult for patients to obtain timely appointments. Why are doctors so burned out? What can we do to address physician burnout? The problem of physician burnout is complex and there is no easy solution in sight.",
            "url": "https://www.health.harvard.edu/blog/physician-burnout-can-affect-your-health-2018062214093",
            "img_url": "https://hhp-blog.s3.amazonaws.com/2018/06/Doctor-Burnout-iStock-Sarinyapinngam_865228192-1024x683.jpg",
            "date": "2018-06-22 10:30:12+00:00",
            "entities": [
                {
                    "label": "United States"
                },
                {
                    "label": "American Association of Medical Colleges"
                },
                {
                    "label": "Mayo Clinic"
                }
            ],
            "concepts": [
                {
                    "label": "Physician"
                },
                {
                    "label": "Medicine"
                },
                {
                    "label": "Hospital"
                }
            ]
        },
        {
            "title": "6 ways to keep your child safe this summer - Harvard Health Blog",
            "summary": "The contents displayed within this public group(s), such as text, graphics, and other material (\"Content\") are intended for educational purposes only. The Content is not intended to substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your healthcare provider with any questions you may have regarding your medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read in a public group(s). If you think you may have a medical emergency, call your healthcare provider or 911 immediately. Please discuss any options with your healthcare provider. The information you share, including that which might otherwise be Protected Health Information, to this site is by design open to the public and is not a private, secure service. You should think carefully before disclosing any personal information in any public forum. As with any public forum on any site, this information may also appear in third-party search engines like Google, MSN, Yahoo, etc.",
            "url": "https://www.health.harvard.edu/blog/6-ways-keep-child-safe-summer-2017071812077",
            "img_url": "https://hhp-blog.s3.amazonaws.com/2017/07/iStock-481761080-Copy-1024x683.jpg",
            "date": "2017-07-18 14:30:59+00:00",
            "entities": [
                {
                    "label": "Harvard University"
                },
                {
                    "label": "Google"
                }
            ],
            "concepts": [
                {
                    "label": "Health care"
                },
                {
                    "label": "Medicine"
                },
                {
                    "label": "Illness"
                }
            ]
        }
    ]
}
```


## Deployment

### Core API (Base Directory)
The microservice is deployed on Google Cloud App engine standard. The service must be deployed on at least a F2 instance, F1 runs out of memory.


Add the url for the language processor API in `config.py`. Also add the URL of the Neo4j graph database.
**Note:** The graph DB url will change when the resource is shut down if the DB is hosted on Google Cloud.


Login to the gcloud cli `gcloud auth login`. Deploy to App Engine with config in `app.yaml` by running `gcloud app deploy app.yaml --project <<YOUR PROJECT ID>>` from the base directory.


### RSS Article Curation Serverless Function
Run `serverless deploy` in the `article_curation` directory

### Cron Jobs Serverless Function
Add the url for the rss downloader endpoint in `cron_jobs/config.py`.


Run `serverless deploy` in the `cron_jobs` directory. Configure the cron job in the GCP console.


## Issues
- The URL of the Compute Engine Neo4j graph can change if instance is shutdown, need to update graph_url variable.
- The newspaper library is modified due to an issue with the parsing. article_downloader.py contains code to extend the original cleaner class. The newspaper Library contains a cleaner class which causes an issue with some websites where the text cannot be extracted. This issue was solved by extending the original cleaner class and removing the cleaning feature when no text is extracted the first time.

