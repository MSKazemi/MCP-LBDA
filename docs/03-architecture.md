# 3️⃣ Architecture and Flow

## Architecture

```mermaid
graph LR
		User[User / Agent] --> LLM[LLM]
		dir[dir]
		MCPClient[MCP Client]
		LLM --> MCPClient
    
    subgraph MCPClient
	    MCPC[MCP Client] --> Roots[Roots]
	    MCPC --> Sampling[Sampling]
		end 

	  
	  
		subgraph MCPServer[MCP Server]
			MCPS[MCP Server] --> Tools[Tools]
			MCPS --> Resources[Resources]
			MCPS --> Prompt[Prompt Templates]
		end 

		MCPClient <--->|"Transport Layer"| MCPServer
		Roots <--> |Opening<br/>Reading<br/>Analyzing| dir
	
	  Tools --> Tool1
	  Tools --> Tool2
```



---

## Request Lifecycle

### Request Flow
```
User → Model → Tool Call → MCP Server → Result → Model → User
```

1. The **user** asks a question.
2. The **model** decides it needs a tool (e.g., "add two numbers").
3. The model calls the **tool** via the MCP client.
4. The **MCP server** runs the tool and returns the result.
5. The model receives the result, reasons, and responds to the user.



1. User: *"What is 7 + 12?"*
2. LLM decides it needs `add(7, 12)`
3. Client sends `tools/call` → `{"name": "add", "arguments": {"a": 7, "b": 12}}`
4. Server runs `add(7, 12)` → `19`
5. Client returns `19` to the LLM
6. LLM responds: *"7 + 12 = 19"*

```mermaid
flowchart TD
    A[User Question] --> B[LLM Analysis]

    B --> C{Needs Tool?}

    C -->|No| D[Respond Directly]
    D --> Z[Final Answer]

    C -->|Yes| E[Create Tool Call]
    E --> F[MCP Client Sends Request]
    F --> G[MCP Server Executes Tool]
    G --> H[Return Result]
    H --> I[LLM Continues Reasoning]
    I --> Z
```

#### More Complete Flow

```mermaid
flowchart TD
    A[User Request] --> B[LLM Generates Plan]
    B --> C{Needs Tool?}

    C -- No --> D[LLM Responds Directly]
    D --> Z[Final Response]

    C -- Yes --> E[MCP Client Sends Tool Call]
    E --> F[MCP Server Receives Request]

    F --> G{Type of Capability?}

    G -->|Prompt| H[Return Prompt Template]
    G -->|Resource| I[Fetch Resource Data]
    G -->|Tool| J[Execute Tool]

    J --> K["Call External System<br/> K8s / DB"]
    K --> J

    H --> L[Return Result to MCP Client]
    I --> L
    J --> L

    L --> M[LLM Continues Reasoning]
    M --> Z[Final Response to User]
```




# 4️⃣ Example: Calculator

User asks:

> What is 7 + 12?

LLM generates structured tool call:

```json
{
  "name": "add",
  "arguments": {"a": 7, "b": 12}
}
```

Server executes:

```python
add(7, 12) → 19
```

Final answer:

> 7 + 12 = 19

---

### Client Options

- **Cursor** or **Claude Desktop** – full LLM integration
- **FastMCP Client** – each example ships a `client.py` using `fastmcp.Client`
- **`examples/01-calculator/demo.py`** – full loop with a simulated LLM


# Teaching Mode

Each example directory contains:

* `server.py`
* `client.py`
* `demo.py` (simulated LLM loop)

The simulated LLM allows you to understand MCP **without needing a real API key**.

---

## Reference
> FastMCP provides both server and client. See [gofastmcp.com](https://gofastmcp.com).


**Next:** [04 – FastMCP Explained](04-fastmcp-explained.md)