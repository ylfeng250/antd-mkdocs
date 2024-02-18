## zh-CN

通过 `image` 指定图片地址。为保证图片高清且不被拉伸，请设置 width 和 height, 并上传至少两倍的宽高的 logo 图片地址。

## en-US

Specify the image address via `image`. To ensure that the image is high definition and not stretched, set the width and height, and upload at least twice the width and height of the logo image address.
```tsx
import React from 'react';
import { Watermark } from 'antd';

const App: React.FC = () => (
  <Watermark
    height={30}
    width={130}
    image="https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*lkAoRbywo0oAAAAAAAAAAAAADrJ8AQ/original"
  >
    <div style={{ height: 500 }} />
  </Watermark>
);

export default App;
```
