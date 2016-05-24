package main

import (
	"encoding/json"
	"testing"
)

var json_1_small = []byte(`{
	"id": 13553,
	"type": "text",
	"field1": 1,
	"field2": 1,
	"field3": 1,
	"field4": [],
	"field5": "stringing",
	"field6": {},
	"field7": "ststringasdf",
	"field8": [1, 2, 3, 4, 5, 6]
}`)

var json_2_small = []byte(`{
	"id": 13553,
	"type": "text",
	"data": {
		"field1": 1,
		"field2": 1,
		"field3": 1,
		"field4": [],
		"field5": "stringing",
		"field6": {},
		"field7": "ststringasdf",
		"field8": [1, 2, 3, 4, 5, 6]
	}
}`)

var json_1_medium = []byte(`{
	"id": 13553,
	"type": "text",
	"field1": 1,
	"field2": 1,
	"field3": 1,
	"field4": [],
	"field5": "stringing",
	"field6": {},
	"field7": "ststringasdf",
	"field8": [1, 2, 3, 4, 5, 6],
	"code": {"widget": {
		"debug": "on",
		"window": {
			"title": "Sample Konfabulator Widget",
			"name": "main_window",
			"width": 500,
			"height": 500
		},
		"image": {
			"src": "Images/Sun.png",
			"name": "sun1",
			"hOffset": 250,
			"vOffset": 250,
			"alignment": "center"
		},
		"text": {
			"data": "Click Here",
			"size": 36,
			"style": "bold",
			"name": "text1",
			"hOffset": 250,
			"vOffset": 100,
			"alignment": "center",
			"onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
		}
	}}
}`)

var json_2_medium = []byte(`{
	"id": 13553,
	"type": "text",
	"data": {
		"field1": 1,
		"field2": 1,
		"field3": 1,
		"field4": [],
		"field5": "stringing",
		"field6": {},
		"field7": "ststringasdf",
		"field8": [1, 2, 3, 4, 5, 6],
		"code": {"widget": {
			"debug": "on",
			"window": {
				"title": "Sample Konfabulator Widget",
				"name": "main_window",
				"width": 500,
				"height": 500
			},
			"image": {
				"src": "Images/Sun.png",
				"name": "sun1",
				"hOffset": 250,
				"vOffset": 250,
				"alignment": "center"
			},
			"text": {
				"data": "Click Here",
				"size": 36,
				"style": "bold",
				"name": "text1",
				"hOffset": 250,
				"vOffset": 100,
				"alignment": "center",
				"onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
			}
		}}
	}
}`)

type Message struct {
	ID   int             `json:"id"`
	Type string          `json:"type"`
	Data json.RawMessage `json:"data"`
}

func TestEqual(t *testing.T) {
	var m1 map[string]interface{}
	json.Unmarshal(json_1_medium, &m1)
	id1, text1 := int(m1["id"].(float64)), m1["type"].(string)

	var m2 Message
	json.Unmarshal(json_2_medium, &m2)
	id2, text2 := m2.ID, m2.Type

	if id1 == id2 && text1 == text2 && id1 == 13553 && text1 == "text" {

	} else {
		t.Fail()
	}

	var m_1 map[string]interface{}
	json.Unmarshal(json_1_small, &m_1)
	id_1, text_1 := int(m_1["id"].(float64)), m_1["type"].(string)

	var m_2 Message
	json.Unmarshal(json_2_small, &m_2)
	id_2, text_2 := m_2.ID, m_2.Type

	if id_1 == id_2 && text_1 == text_2 && id_1 == 13553 && text_1 == "text" {

	} else {
		t.Fail()
	}
}

func Benchmark_json1_small(b *testing.B) {
	for i := 0; i < b.N; i++ {
		var m1 map[string]interface{}
		json.Unmarshal(json_1_small, &m1)
		_, _ = int(m1["id"].(float64)), m1["type"].(string)
	}
}

func Benchmark_json2_small(b *testing.B) {
	for i := 0; i < b.N; i++ {
		var m2 Message
		json.Unmarshal(json_2_small, &m2)
		_, _ = m2.ID, m2.Type
	}
}

func Benchmark_json1_medium(b *testing.B) {
	for i := 0; i < b.N; i++ {
		var m1 map[string]interface{}
		json.Unmarshal(json_1_medium, &m1)
		_, _ = int(m1["id"].(float64)), m1["type"].(string)
	}
}

func Benchmark_json2_medium(b *testing.B) {
	for i := 0; i < b.N; i++ {
		var m2 Message
		json.Unmarshal(json_2_medium, &m2)
		_, _ = m2.ID, m2.Type
	}
}
