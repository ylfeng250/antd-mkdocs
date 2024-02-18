## zh-CN

位置有十二个方向。如需箭头指向目标元素中心，可以设置 `arrow: { pointAtCenter: true }`。

## en-US

There are 12 `placement` options available. Use `arrow: { pointAtCenter: true }` if you want the arrow to point at the center of target.

<style>
#components-popconfirm-demo-placement .ant-btn {
  margin-left: 0;
  margin-right: 8px;
  margin-bottom: 8px;
  width: 70px;
  text-align: center;
  padding: 0;
}
#components-popconfirm-demo-placement .ant-btn-rtl {
  margin-left: 8px;
  margin-right: 0;
}
</style>
```tsx
import React from 'react';
import { Button, Popconfirm, ConfigProvider } from 'antd';

const text = 'Are you sure to delete this task?';
const description = 'Delete the task';
const buttonWidth = 80;

const App: React.FC = () => (
  <ConfigProvider
    button={{
      style: { width: buttonWidth, margin: 4 },
    }}
  >
    <div className="demo">
      <div style={{ marginInlineStart: buttonWidth, whiteSpace: 'nowrap' }}>
        <Popconfirm
          placement="topLeft"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>TL</Button>
        </Popconfirm>
        <Popconfirm
          placement="top"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>Top</Button>
        </Popconfirm>
        <Popconfirm
          placement="topRight"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>TR</Button>
        </Popconfirm>
      </div>
      <div style={{ width: buttonWidth, float: 'inline-start' }}>
        <Popconfirm
          placement="leftTop"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>LT</Button>
        </Popconfirm>
        <Popconfirm
          placement="left"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>Left</Button>
        </Popconfirm>
        <Popconfirm
          placement="leftBottom"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>LB</Button>
        </Popconfirm>
      </div>
      <div style={{ width: buttonWidth, marginInlineStart: buttonWidth * 4 + 24 }}>
        <Popconfirm
          placement="rightTop"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>RT</Button>
        </Popconfirm>
        <Popconfirm
          placement="right"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>Right</Button>
        </Popconfirm>
        <Popconfirm
          placement="rightBottom"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>RB</Button>
        </Popconfirm>
      </div>
      <div style={{ marginInlineStart: buttonWidth, clear: 'both', whiteSpace: 'nowrap' }}>
        <Popconfirm
          placement="bottomLeft"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>BL</Button>
        </Popconfirm>
        <Popconfirm
          placement="bottom"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>Bottom</Button>
        </Popconfirm>
        <Popconfirm
          placement="bottomRight"
          title={text}
          description={description}
          okText="Yes"
          cancelText="No"
        >
          <Button>BR</Button>
        </Popconfirm>
      </div>
    </div>
  </ConfigProvider>
);

export default App;
```
