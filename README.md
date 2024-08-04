# Table of Contents

- [Overview](#overview)
- [Step 1: Define a data collection & add objects](#step1)
- [Step 2: Semantic Search](#step2)
- [Step 3: Semantic Search with a Filter](#step3)
- [Step 4: Generative search (single prompt)](#step4)
- [Step 5: Generative search (grouped task)](#step5)
- [Recap](#recap)
- [Next Steps](#next-steps)

# Overview
Welcome to the Quickstart guide for Weaviate, an open-source vector database. This tutorial is intended to be a hands-on introduction to Weaviate.

This Quickstart takes about 20 minutes to complete. It introduces some common tasks:

* Build a Weaviate vector database.
* Make a semantic search query.
* Add a filter to your query.
* Use generative searches and a large language model (LLM) to transform your search results.

## Object vectors
Vectors are mathematical representations of data objects, which enable similarity-based searches in vector databases like Weaviate.

With Weaviate, you have options to:

* Have **Weaviate create vectors** for you, or
* Specify **custom vectors.**

This tutorial demonstrates having Weaviate create vectors with a vectorizer. For a tutorial on using custom vectors, see this tutorial.

## Source data
<details>
  <summary> We will use a (tiny) dataset of quizzes. </summary>

|   | Category | Question | Answer |
| - | -------- | -------- | ------ |
| 0 | SCIENCE  | This organ removes excess glucose from the blood & stores it as glycogen | Liver |
| 1 | ANIMALS  | It's the only living mammal in the order Proboseidea	| Elephant |
| 2 | ANIMALS  | The gavial looks very much like a crocodile except for this bodily feature	 | the nose or snout |
| 3 | ANIMALS  | Weighing around a ton, the eland is the largest species of this animal in Africa	| Antelope |
| 4 | ANIMALS  | Heaviest of all poisonous snakes is this North American rattlesnake	| the diamondback rattler |
| 5 | SCIENCE  | 2000 news: the Gunnison sage grouse isn't just another northern sage grouse, but a new one of this classification	| species |
| 6 | SCIENCE  | A metal that is "ductile" can be pulled into this while cold & under pressure	| wire |
| 7 | SCIENCE  | In 1953 Watson & Crick built a model of the molecular structure of this, the gene-carrying substance	| DNA |
| 8 | SCIENCE  | Changes in the tropospheric layer of this are what gives us weather	| the atmosphere |
| 9 | SCIENCE  | In 70-degree air, a plane traveling at about 1,130 feet per second breaks it	| Sound barrier |
</details><br>

# <div id="step0"/> Step 0: Setup your OPENAI API Key

In the file that opes, provide your OPENAI API key

* Run `$ open openai_apikey.sh`
* Run `$ ./openai_apikey.sh`

# <div id="step1"/> Step 1: Define a data collection & add objects 

We define a data collection (a "collection" in Weaviate) to store objects in. This is analogous to creating a table in relational (SQL) databases.

* Run `$ open load.py`
* Run `$ python3 load.py`

The above code will:

* Configures a collection object with:
  *  Name `Question`
  * Integrations with OpenAI [embedding](https://weaviate.io/developers/weaviate/model-providers/openai/embeddings) and [generative](https://weaviate.io/developers/weaviate/model-providers/openai/generative) AI models
* Then creates the collection.
* Add objects to Weaviate using a batch import ([read more](https://weaviate.io/developers/weaviate/manage-data/import)) process for maximum efficiency.

* Loads objects, and
* Adds objects to the target collection (`Question`) one by one.

Now, let's run some queries on your Weaviate instance. Weaviate powers many different types of searches. We will try a few here.

# <div id="step2"/> Step 2: Semantic Search

Let's start with a similarity search. A `nearText` search looks for objects in Weaviate whose vectors are most similar to the vector for the given input text.

* Run `$ open semantic_search.py`
* Run `$ python3 semantic_search.py`


<details>
  <summary>You should see results similar to this:</summary>
```
{
    "data": {
        "Get": {
            "Question": [
                {
                    "answer": "DNA",
                    "category": "SCIENCE",
                    "question": "In 1953 Watson & Crick built a model of the molecular structure of this, the gene-carrying substance"
                },
                {
                    "answer": "Liver",
                    "category": "SCIENCE",
                    "question": "This organ removes excess glucose from the blood & stores it as glycogen"
                }
            ]
        }
    }
}
```
</details><br>

The response includes a list of objects whose vectors are most similar to the word `biology`. The top 2 results are returned here as we have set a `limit` to `2`.

> 📘 **WHY IS THIS USEFUL?**
>
> Notice that even though the word `biology` does not appear anywhere, Weaviate returns biology-related entries.
> This example shows why vector searches are powerful. Vectorized data objects allow for searches based on degrees of similarity, as shown here.

# <div id="step3"/> Step 3: Semantic Search with a Filter

You can add Boolean filters to searches. For example, the above search can be modified to only in objects that have a "category" value of "ANIMALS". Run the following code to see the results:

* Run `$ open semantic_search_with_filter.py`
* Run `$ python3 semantic_search_with_filter.py`

<details>
  <summary>You should see results similar to this:</summary>
```
{
    "data": {
        "Get": {
            "Question": [
                {
                    "answer": "Elephant",
                    "category": "ANIMALS",
                    "question": "It's the only living mammal in the order Proboseidea"
                },
                {
                    "answer": "the nose or snout",
                    "category": "ANIMALS",
                    "question": "The gavial looks very much like a crocodile except for this bodily feature"
                }
            ]
        }
    }
}
```
</details><br>

The results are limited to objects from the `ANIMALS` category.

> 📘 **WHY IS THIS USEFUL?**
>
> Using a Boolean filter allows you to combine the flexibility of vector search with the precision of `where` filters.

# <div id="step4"/> Step 4: Generative search (single prompt)

Next, let's try a generative search. A generative search, also called retrieval augmented generation, prompts a large language model (LLM) with a combination of a user query as well as data retrieved from a database.

* Run `$ open generative_search.py`
* Run `$ python3 generative_search.py`

Note that the code uses a `single prompt` query, which asks the model generate an answer for each retrieved database object.

<details>
  <summary>You should see results similar to this:</summary>
```
{
    "data": {
        "Get": {
            "Question": [
                {
                    "_additional": {
                        "generate": {
                            "error": null,
                            "singleResult": "DNA is like a special code that tells our bodies how to grow and work. It's like a recipe book that has all the instructions for making you who you are. Just like a recipe book has different recipes for different foods, DNA has different instructions for making different parts of your body, like your eyes, hair, and even your personality! It's really amazing because it's what makes you unique and special."
                        }
                    },
                    "answer": "DNA",
                    "category": "SCIENCE",
                    "question": "In 1953 Watson & Crick built a model of the molecular structure of this, the gene-carrying substance"
                },
                {
                    "_additional": {
                        "generate": {
                            "error": null,
                            "singleResult": "Well, a species is a group of living things that are similar to each other in many ways. They have the same kind of body parts, like legs or wings, and they can have babies with other members of their species. For example, dogs are a species, and so are cats. They look different and act differently, but all dogs can have puppies with other dogs, and all cats can have kittens with other cats. So, a species is like a big family of animals or plants that are all related to each other in a special way."
                        }
                    },
                    "answer": "species",
                    "category": "SCIENCE",
                    "question": "2000 news: the Gunnison sage grouse isn't just another northern sage grouse, but a new one of this classification"
                }
            ]
        }
    }
}
```

</details><br>

We see that Weaviate has retrieved the same results as before. But now it includes an additional, generated text with a plain-language explanation of each answer.

# <div id="step5"/> Step 5: Generative search (grouped task)
The next example uses a grouped task prompt instead to combine all search results and send them to the LLM with a prompt.

* Run `$ open generative_search_grouped.py`
* Run `$ python3 generative_search_grouped.py`

The first returned object will include the generated text. Here's one that we got:

```
🧬 In 1953, Watson & Crick 🧪 built a model of the molecular structure of DNA, the gene-carrying substance! 🧬

🐦🔍 2000 news: The Gunnison sage grouse isn't just another northern sage grouse, but a new species of its own! 🆕🐔 #ScienceFacts
```

> 📘 **WHY IS THIS USEFUL?**
> 
> Generative search sends retrieved data from Weaviate to a large language model, or LLM. This allows you to go beyond simple data retrieval, but transform the data into a more useful form, without ever leaving Weaviate.

# Recap
Well done! You have:

* Created your own cloud-based vector database with Weaviate,
* Populated it with data objects using an inference API,
* Performed searches, including:
  * Semantic search,
  * Semantic search with a filter and
  * Generative search.

Where next is up to you. We include a few links below.

# Next Steps
You can do much more with Weaviate. We suggest trying:

* Examples from our [search how-to](https://weaviate.io/developers/weaviate/search) guides for [keyword](https://weaviate.io/developers/weaviate/search/bm25), [similarity](https://weaviate.io/developers/weaviate/search/similarity), [hybrid](https://weaviate.io/developers/weaviate/search/hybrid), [generative](https://weaviate.io/developers/weaviate/search/generative) searches and [filters](https://weaviate.io/developers/weaviate/search/filters) or
* Learning [how to manage data](https://weaviate.io/developers/weaviate/manage-data), like [reading](https://weaviate.io/developers/weaviate/manage-data/read), [batch importing](https://weaviate.io/developers/weaviate/manage-data/import), [updating](https://weaviate.io/developers/weaviate/manage-data/update), [deleting](https://weaviate.io/developers/weaviate/manage-data/delete) objects or [bulk exporting](https://weaviate.io/developers/weaviate/manage-data/read-all-objects) data.

For more holistic learning, try [Weaviate Academy](https://weaviate.io/developers/academy). We have built free courses for you to learn about Weaviate and the world of vector search.

You can also try a larger, [1,000 row](https://raw.githubusercontent.com/databyjp/wv_demo_uploader/main/weaviate_datasets/data/jeopardy_1k.json) version of the Jeopardy! dataset, or [this tiny set of 50 wine reviews](https://raw.githubusercontent.com/databyjp/wv_demo_uploader/main/weaviate_datasets/data/winemag_tiny.csv).