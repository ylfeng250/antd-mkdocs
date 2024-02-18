## zh-CN

测试一些 `style` 修改样式的行为。

## en-US

Use `style` to change default style.
```tsx
import React from 'react';
import { Divider } from 'antd';

const App: React.FC = () => (
  <>
    <Divider style={{ borderWidth: 2, borderColor: '#7cb305' }} />
    <Divider style={{ borderColor: '#7cb305' }} dashed />
    <Divider style={{ borderColor: '#7cb305' }} dashed>
      Text
    </Divider>
    <Divider type="vertical" style={{ height: 60, borderColor: '#7cb305' }} />
    <Divider type="vertical" style={{ height: 60, borderColor: '#7cb305' }} dashed />

    <div style={{ display: 'flex', flexDirection: 'column', height: 50, boxShadow: '0 0 1px red' }}>
      <Divider style={{ background: 'rgba(0,255,0,0.05)' }} orientation="left">
        Text
      </Divider>
    </div>
  </>
);

export default App;
```
