## zh-CN

自定义预览文本。

## en-US

Custom preview mask.

```css
.customize-mask {
  font-size: 20px;
  opacity: 1;
}
.customize-mask .anticon {
  font-size: 32px;
}
```
```tsx
import React from 'react';
import { ZoomInOutlined } from '@ant-design/icons';
import { Image, Space } from 'antd';

const App: React.FC = () => (
  <Image
    width={96}
    src="https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png"
    preview={{
      maskClassName: 'customize-mask',
      mask: (
        <Space direction="vertical" align="center">
          <ZoomInOutlined />
          示例
        </Space>
      ),
    }}
  />
);

export default App;
```
